import React, { useState } from "react";
import { Link, useNavigate, useLocation } from "react-router-dom";
import { resetPassword } from "../api/endpoints.js";
import { useAppSettings } from "../context/AppSettingsContext.jsx";

export default function ResetPassword() {
  const { t } = useAppSettings();
  const navigate = useNavigate();
  const location = useLocation();

  const [email, setEmail] = useState(location.state?.email || "");
  const [code, setCode] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

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
      await resetPassword(email, code, newPassword);
      setSuccess(true);
      setTimeout(() => navigate("/login"), 1500);
    } catch (err) {
      const detail = err?.response?.data?.detail || "Reset failed. Please check your code and try again.";
      setError(detail);
    } finally {
      setLoading(false);
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
          <h1 className="text-xl font-bold mb-1">Enter your reset code</h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mb-5">
            Check your email for a 6-digit code, then choose a new password.
          </p>

          {error && (
            <div className="mb-4 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-2.5 rounded-xl">
              {error}
            </div>
          )}
          {success && (
            <div className="mb-4 text-sm bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-400 px-4 py-2.5 rounded-xl">
              Password reset! Redirecting to login...
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">{t("email")}</label>
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="input-field"
                placeholder="you@example.com"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Reset code</label>
              <input
                type="text"
                inputMode="numeric"
                maxLength={6}
                required
                value={code}
                onChange={(e) => setCode(e.target.value.replace(/\D/g, ""))}
                className="input-field tracking-widest"
                placeholder="123456"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">New password</label>
              <input
                type="password"
                required
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                className="input-field"
                placeholder="••••••••"
              />
            </div>
            <button type="submit" disabled={loading || success} className="btn-primary w-full">
              {loading ? "..." : "Reset password"}
            </button>
          </form>

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
