import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { forgotPassword } from "../api/endpoints.js";
import { useAppSettings } from "../context/AppSettingsContext.jsx";

export default function ForgotPassword() {
  const { t } = useAppSettings();
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await forgotPassword(email);
      // Always shown, regardless of whether the email exists — the backend
      // intentionally never reveals that, so this page doesn't either.
      setSubmitted(true);
    } catch (err) {
      const detail = err?.response?.data?.detail || "Something went wrong. Please try again.";
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
          <h1 className="text-xl font-bold mb-1">Reset your password</h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mb-5">
            Enter your account email and we'll send you a reset code.
          </p>

          {error && (
            <div className="mb-4 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-2.5 rounded-xl">
              {error}
            </div>
          )}

          {submitted ? (
            <div className="space-y-4">
              <div className="text-sm bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-400 px-4 py-2.5 rounded-xl">
                If that email is registered, a reset code is on its way. Check your inbox.
              </div>
              <button
                type="button"
                className="btn-primary w-full"
                onClick={() => navigate("/reset-password", { state: { email } })}
              >
                I have my code
              </button>
            </div>
          ) : (
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
              <button type="submit" disabled={loading} className="btn-primary w-full">
                {loading ? "..." : "Send reset code"}
              </button>
            </form>
          )}

          <p className="mt-5 text-sm text-center text-slate-600 dark:text-slate-400">
            Remembered your password?{" "}
            <Link to="/login" className="text-brand-600 font-semibold hover:underline">
              {t("login")}
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}
