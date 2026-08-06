import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";

export default function Register() {
  const { register } = useAuth();
  const { t } = useAppSettings();
  const navigate = useNavigate();

  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [preferredLanguage, setPreferredLanguage] = useState("en");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    const trimmedName = fullName.trim().replace(/\s+/g, " ");

    if (trimmedName.length < 2) {
      setError("Please enter your full name.");
      return;
    }
    if (password.length < 6) {
      setError("Password must be at least 6 characters.");
      return;
    }

    setLoading(true);
    try {
      await register(trimmedName, email, password, preferredLanguage);
      navigate("/dashboard");
    } catch (err) {
      const detail = err?.response?.data?.detail || "Registration failed. Please try again.";
      setError(detail);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-900 px-4 py-8">
      <div className="w-full max-w-sm">
        <div className="text-center mb-6">
          <Link to="/" className="inline-flex items-center gap-2 font-bold text-xl">
            <span className="text-brand-600">🎓</span>
            <span>{t("appName")}</span>
          </Link>
        </div>

        <div className="card">
          <h1 className="text-xl font-bold mb-1">{t("createAccount")}</h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mb-5">
            Start learning Python, SQLite, FastAPI, Linux, and Git today.
          </p>

          {error && (
            <div className="mb-4 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-2.5 rounded-xl">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">{t("fullName")}</label>
              <input
                type="text"
                name="fullName"
                autoComplete="name"
                required
                minLength={2}
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                className="input-field"
                placeholder="e.g. Aisha Bello"
              />
            </div>
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
              <label className="block text-sm font-medium mb-1">{t("password")}</label>
              <input
                type="password"
                required
                minLength={6}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="input-field"
                placeholder="At least 6 characters"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">{t("language")}</label>
              <select
                value={preferredLanguage}
                onChange={(e) => setPreferredLanguage(e.target.value)}
                className="input-field"
              >
                <option value="en">English</option>
                <option value="ha">Hausa</option>
              </select>
            </div>
            <button type="submit" disabled={loading} className="btn-primary w-full">
              {loading ? "..." : t("createAccount")}
            </button>
          </form>

          <p className="mt-5 text-sm text-center text-slate-600 dark:text-slate-400">
            Already have an account?{" "}
            <Link to="/login" className="text-brand-600 font-semibold hover:underline">
              {t("login")}
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}
