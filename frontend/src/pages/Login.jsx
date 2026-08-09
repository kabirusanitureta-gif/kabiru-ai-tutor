import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";

export default function Login() {
  const { login, loginWithPasskey, webauthnSupported } = useAuth();
  const { t } = useAppSettings();
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [passkeyLoading, setPasskeyLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const normalizedEmail = email.trim().toLowerCase();
      await login(normalizedEmail, password);
      navigate("/dashboard");
    } catch (err) {
      const detail =
        err?.response?.data?.detail ||
        "Login failed. Please check your credentials.";
      setError(detail);
    } finally {
      setLoading(false);
    }
  };

  const handlePasskeyLogin = async () => {
    setError("");
    setPasskeyLoading(true);

    try {
      const normalizedEmail = email.trim().toLowerCase();
      await loginWithPasskey(normalizedEmail || undefined);
      navigate("/dashboard");
    } catch (err) {
      if (err?.name !== "NotAllowedError") {
        const detail =
          err?.response?.data?.detail ||
          "Face ID / Touch ID sign-in failed. Please use your password.";
        setError(detail);
      }
    } finally {
      setPasskeyLoading(false);
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
            {t("welcomeBack")}
          </h1>

          <p className="text-sm text-slate-500 dark:text-slate-400 mb-5">
            Log in to continue your learning journey.
          </p>

          {error && (
            <div className="mb-4 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-2.5 rounded-xl">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">
                {t("email")}
              </label>

              <input
                type="email"
                name="email"
                id="login-email"
                required
                autoComplete="email"
                inputMode="email"
                spellCheck="false"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="input-field w-full"
                placeholder="you@example.com"
              />
            </div>

            <div>
              <div className="flex items-center justify-between mb-1">
                <label className="block text-sm font-medium">
                  {t("password")}
                </label>

                <Link
                  to="/forgot-password"
                  className="text-xs text-brand-600 hover:underline"
                >
                  Forgot password?
                </Link>
              </div>

              <div className="relative">
                <input
                  type={showPassword ? "text" : "password"}
                  name="password"
                  id="login-password"
                  required
                  autoComplete="current-password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="input-field pr-12 w-full"
                  placeholder="••••••••"
                />

                <button
                  type="button"
                  onClick={() => setShowPassword((prev) => !prev)}
                  aria-label={
                    showPassword ? "Hide password" : "Show password"
                  }
                  aria-pressed={showPassword}
                  className="absolute inset-y-0 right-0 flex items-center px-3 text-lg touch-manipulation"
                >
                  {showPassword ? "🙈" : "👁️"}
                </button>
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="btn-primary w-full"
            >
              {loading ? "..." : t("login")}
            </button>
          </form>

          {webauthnSupported && (
            <>
              <div className="flex items-center gap-3 my-4">
                <div className="h-px flex-1 bg-slate-200 dark:bg-slate-700" />
                <span className="text-xs text-slate-400">or</span>
                <div className="h-px flex-1 bg-slate-200 dark:bg-slate-700" />
              </div>

              <button
                type="button"
                onClick={handlePasskeyLogin}
                disabled={passkeyLoading}
                className="btn-secondary w-full flex items-center justify-center gap-2"
              >
                <span>🆔</span>
                {passkeyLoading
                  ? "..."
                  : "Sign in with Face ID / Touch ID"}
              </button>
            </>
          )}

          <p className="mt-5 text-sm text-center text-slate-600 dark:text-slate-400">
            Don't have an account?{" "}
            <Link
              to="/register"
              className="text-brand-600 font-semibold hover:underline"
            >
              {t("register")}
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}
