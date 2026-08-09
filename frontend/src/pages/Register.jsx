import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Eye, EyeOff } from "lucide-react";
import { useAuth } from "../context/AuthContext.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";

export default function Register() {
  const { register } = useAuth();
  const { t } = useAppSettings();
  const navigate = useNavigate();

  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [preferredLanguage, setPreferredLanguage] = useState("en");

  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    const name = fullName.trim().replace(/\s+/g, " ");
    const userEmail = email.trim().toLowerCase();

    if (name.length < 2) {
      setError("Please enter your full name.");
      return;
    }

    if (password.length < 6) {
      setError("Password must be at least 6 characters.");
      return;
    }

    if (password !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    setLoading(true);

    try {
      await register(name, userEmail, password, preferredLanguage);
      navigate("/dashboard");
    } catch (err) {
      const detail =
        err?.response?.data?.detail ||
        err?.message ||
        "Registration failed. Please try again.";

      setError(
        Array.isArray(detail)
          ? detail.map((item) => item?.msg || String(item)).join(", ")
          : String(detail)
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-900 px-4 py-8">
      <div className="w-full max-w-md">

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

          <h1 className="text-2xl font-bold mb-1">
            {t("createAccount")}
          </h1>

          <p className="text-sm text-slate-500 dark:text-slate-400 mb-6">
            Create your account and start learning today.
          </p>

          {error && (
            <div className="mb-4 rounded-xl bg-red-50 dark:bg-red-900/20 px-4 py-3 text-sm text-red-600 dark:text-red-400">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">

            {/* Full Name */}
            <div>
              <label className="block text-sm font-medium mb-1">
                {t("fullName")}
              </label>

              <input
                type="text"
                name="fullName"
                autoComplete="name"
                required
                minLength={2}
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                className="input-field"
                placeholder="Enter your full name"
              />
            </div>

            {/* Email */}
            <div>
              <label className="block text-sm font-medium mb-1">
                {t("email")}
              </label>

              <input
                type="email"
                name="email"
                autoComplete="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="input-field"
                placeholder="Enter your email"
              />
            </div>

            {/* Password */}
            <div>
              <label className="block text-sm font-medium mb-1">
                {t("password")}
              </label>

              <div className="relative">
                <input
                  type={showPassword ? "text" : "password"}
                  name="password"
                  autoComplete="new-password"
                  required
                  minLength={6}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="input-field pr-12"
                  placeholder="At least 6 characters"
                />

                <button
                  type="button"
                  onClick={() => setShowPassword((value) => !value)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300"
                  aria-label={showPassword ? "Hide password" : "Show password"}
                >
                  {showPassword ? (
                    <EyeOff size={20} />
                  ) : (
                    <Eye size={20} />
                  )}
                </button>
              </div>
            </div>

            {/* Confirm Password */}
            <div>
              <label className="block text-sm font-medium mb-1">
                Confirm Password
              </label>

              <div className="relative">
                <input
                  type={showConfirmPassword ? "text" : "password"}
                  name="confirmPassword"
                  autoComplete="new-password"
                  required
                  minLength={6}
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  className="input-field pr-12"
                  placeholder="Re-enter your password"
                />

                <button
                  type="button"
                  onClick={() =>
                    setShowConfirmPassword((value) => !value)
                  }
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300"
                  aria-label={
                    showConfirmPassword
                      ? "Hide confirm password"
                      : "Show confirm password"
                  }
                >
                  {showConfirmPassword ? (
                    <EyeOff size={20} />
                  ) : (
                    <Eye size={20} />
                  )}
                </button>
              </div>
            </div>

            {/* Language */}
            <div>
              <label className="block text-sm font-medium mb-1">
                {t("language")}
              </label>

              <select
                value={preferredLanguage}
                onChange={(e) => setPreferredLanguage(e.target.value)}
                className="input-field"
              >
                <option value="en">English</option>
                <option value="ha">Hausa</option>
              </select>
            </div>

            {/* Register */}
            <button
              type="submit"
              disabled={loading}
              className="btn-primary w-full disabled:opacity-60"
            >
              {loading ? "Creating account..." : t("createAccount")}
            </button>
          </form>

          <p className="mt-5 text-sm text-center text-slate-600 dark:text-slate-400">
            Already have an account?{" "}
            <Link
              to="/login"
              className="text-brand-600 font-semibold hover:underline"
            >
              {t("login")}
            </Link>
          </p>

        </div>
      </div>
    </div>
  );
}
