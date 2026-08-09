import React, { useEffect, useState } from "react";
import { Link, useNavigate, useLocation } from "react-router-dom";
import { Eye, EyeOff } from "lucide-react";
import { resetPassword, resendResetCode } from "../api/endpoints.js";
import { useAppSettings } from "../context/AppSettingsContext.jsx";

const RESEND_COOLDOWN = 60;

export default function ResetPassword() {
  const { t } = useAppSettings();
  const navigate = useNavigate();
  const location = useLocation();

  const [email, setEmail] = useState(location.state?.email || "");
  const [code, setCode] = useState("");
  const [newPassword, setNewPassword] = useState("");

  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [resending, setResending] = useState(false);
  const [success, setSuccess] = useState(false);
  const [cooldown, setCooldown] = useState(0);

  useEffect(() => {
    if (cooldown <= 0) return;

    const timer = setInterval(() => {
      setCooldown((value) => (value > 0 ? value - 1 : 0));
    }, 1000);

    return () => clearInterval(timer);
  }, [cooldown]);

  const handleResend = async () => {
    const normalizedEmail = email.trim().toLowerCase();

    if (!normalizedEmail) {
      setError("Enter your email address first.");
      return;
    }

    setError("");
    setMessage("");
    setResending(true);

    try {
      await resendResetCode(normalizedEmail);
      setMessage("If that email is registered, a new reset code has been sent.");
      setCooldown(RESEND_COOLDOWN);
    } catch (err) {
      setError(
        err?.response?.data?.detail ||
        "Could not resend the code. Please try again shortly."
      );
    } finally {
      setResending(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setMessage("");

    const normalizedEmail = email.trim().toLowerCase();

    if (!normalizedEmail) {
      setError("Enter your email address.");
      return;
    }

    if (code.length !== 6) {
      setError("Enter the 6-digit code from your email.");
      return;
    }

    if (newPassword.length < 6) {
      setError("Password must be at least 6 characters.");
      return;
    }

    setLoading(true);

    try {
      await resetPassword(normalizedEmail, code, newPassword);
      setSuccess(true);

      setTimeout(() => {
        navigate("/login", { replace: true });
      }, 1500);
    } catch (err) {
      setError(
        err?.response?.data?.detail ||
        "Reset failed. Please check your code and try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-900 px-4">
      <div className="w-full max-w-sm">

        <div className="text-center mb-6">
          <Link
            to="/"
            className="inline-flex items-center gap-2 font-bold text-xl"
          >
            <span className="text-brand-600">🎓</span>
            <span>{t("appName")}</span>
          </Link>
        </div>

        <div className="card">
          <h1 className="text-xl font-bold mb-1">
            Reset your password
          </h1>

          <p className="text-sm text-slate-500 dark:text-slate-400 mb-5">
            Enter the 6-digit code sent to your email and choose a new password.
          </p>

          {error && (
            <div className="mb-4 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-2.5 rounded-xl">
              {error}
            </div>
          )}

          {message && (
            <div className="mb-4 text-sm bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-400 px-4 py-2.5 rounded-xl">
              {message}
            </div>
          )}

          {success && (
            <div className="mb-4 text-sm bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-400 px-4 py-2.5 rounded-xl">
              Password reset successfully! Redirecting to login...
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">

            <div>
              <label className="block text-sm font-medium mb-1">
                {t("email")}
              </label>

              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="input-field"
                placeholder="Enter your email"
                autoComplete="email"
              />
            </div>

            <div>
              <label className="block text-sm font-medium mb-1">
                Reset code
              </label>

              <input
                type="text"
                inputMode="numeric"
                maxLength={6}
                required
                value={code}
                onChange={(e) =>
                  setCode(e.target.value.replace(/\D/g, ""))
                }
                className="input-field tracking-widest"
                placeholder="Enter 6-digit code"
                autoComplete="one-time-code"
              />
            </div>

            <div>
              <label className="block text-sm font-medium mb-1">
                New password
              </label>

              <div className="relative">
                <input
                  type={showPassword ? "text" : "password"}
                  required
                  minLength={6}
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                  className="input-field pr-12"
                  placeholder="Enter new password"
                  autoComplete="new-password"
                />

                <button
                  type="button"
                  onClick={() => setShowPassword((value) => !value)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300"
                  aria-label={
                    showPassword ? "Hide password" : "Show password"
                  }
                >
                  {showPassword ? (
                    <EyeOff size={20} />
                  ) : (
                    <Eye size={20} />
                  )}
                </button>
              </div>
            </div>

            <button
              type="submit"
              disabled={loading || success}
              className="btn-primary w-full disabled:opacity-60"
            >
              {loading ? "Resetting..." : "Reset password"}
            </button>
          </form>

          <div className="mt-4 text-center">
            <button
              type="button"
              onClick={handleResend}
              disabled={resending || cooldown > 0 || !email.trim()}
              className="text-sm text-brand-600 font-semibold hover:underline disabled:opacity-50 disabled:no-underline"
            >
              {cooldown > 0
                ? `Resend code in ${cooldown}s`
                : resending
                ? "Sending..."
                : "Resend reset code"}
            </button>
          </div>

          <p className="mt-5 text-sm text-center text-slate-600 dark:text-slate-400">
            <Link
              to="/login"
              className="text-brand-600 font-semibold hover:underline"
            >
              Back to {t("login")}
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}
