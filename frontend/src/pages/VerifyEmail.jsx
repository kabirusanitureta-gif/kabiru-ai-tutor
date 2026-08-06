import React, { useEffect, useState } from "react";
import { Link, useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";
import { verifyEmail, resendVerification } from "../api/endpoints.js";

const RESEND_COOLDOWN_SECONDS = 60;

export default function VerifyEmail() {
  const { t } = useAppSettings();
  const { user, updateLocalUser, isAuthenticated } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  // Works right after registration (location.state.email) or if the user
  // navigates here later while logged in but still unverified.
  const [email] = useState(location.state?.email || user?.email || "");
  const [pin, setPin] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [resending, setResending] = useState(false);
  const [resendMessage, setResendMessage] = useState("");
  const [cooldown, setCooldown] = useState(0);

  useEffect(() => {
    // Already verified? Nothing to do here.
    if (isAuthenticated && user?.is_verified) {
      navigate("/dashboard", { replace: true });
    }
  }, [isAuthenticated, user, navigate]);

  useEffect(() => {
    if (cooldown <= 0) return;
    const id = setInterval(() => setCooldown((c) => c - 1), 1000);
    return () => clearInterval(id);
  }, [cooldown]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    if (!email) {
      setError("We couldn't find your email. Please log in again.");
      return;
    }
    if (pin.length !== 6) {
      setError("Enter the 6-digit PIN from your email.");
      return;
    }

    setLoading(true);
    try {
      const res = await verifyEmail(email, pin);
      if (isAuthenticated) {
        updateLocalUser(res.data);
      }
      navigate("/dashboard", { replace: true });
    } catch (err) {
      const detail = err?.response?.data?.detail || "Could not verify that PIN. Please try again.";
      setError(detail);
    } finally {
      setLoading(false);
    }
  };

  const handleResend = async () => {
    if (cooldown > 0 || !email) return;
    setResending(true);
    setResendMessage("");
    setError("");
    try {
      await resendVerification(email);
      setResendMessage("A new PIN has been sent to your email.");
      setCooldown(RESEND_COOLDOWN_SECONDS);
    } catch {
      setResendMessage("Could not resend right now. Please try again shortly.");
    } finally {
      setResending(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-900 px-4">
      <div className="w-full max-w-sm">
        <div className="text-center mb-6">
          <Link to="/" className="inline-flex items-center gap-2 font-bold text-xl">
            <span className="text-brand-600">🎓</span>
            <span>{t("appName")}</span>
          </Link>
        </div>

        <div className="card">
          <h1 className="text-xl font-bold mb-1">Verify your email</h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mb-5">
            We sent a 6-digit PIN to <span className="font-semibold">{email || "your email"}</span>.
            Enter it below to activate your account.
          </p>

          {error && (
            <div className="mb-4 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-2.5 rounded-xl">
              {error}
            </div>
          )}
          {resendMessage && (
            <div className="mb-4 text-sm bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-400 px-4 py-2.5 rounded-xl">
              {resendMessage}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">Verification PIN</label>
              <input
                type="text"
                inputMode="numeric"
                maxLength={6}
                required
                autoComplete="off"
                value={pin}
                onChange={(e) => setPin(e.target.value.replace(/\D/g, ""))}
                className="input-field tracking-widest text-center text-lg"
                placeholder="123456"
              />
            </div>
            <button type="submit" disabled={loading} className="btn-primary w-full">
              {loading ? "..." : "Verify"}
            </button>
          </form>

          <button
            onClick={handleResend}
            disabled={resending || cooldown > 0 || !email}
            className="mt-4 text-sm text-brand-600 font-semibold hover:underline disabled:opacity-50 disabled:no-underline w-full text-center"
          >
            {cooldown > 0 ? `Resend PIN in ${cooldown}s` : resending ? "Sending..." : "Resend PIN"}
          </button>

          <p className="mt-5 text-sm text-center text-slate-600 dark:text-slate-400">
            <Link to="/login" className="text-brand-600 font-semibold hover:underline">
              Back to {t("login")}
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}
