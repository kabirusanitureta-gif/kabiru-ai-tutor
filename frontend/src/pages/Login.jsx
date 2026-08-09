import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext.jsx";
import { Eye, EyeOff } from "lucide-react";
import { useAppSettings, SUPPORTED_LANGUAGES } from "../context/AppSettingsContext";

export default function Login() {
  const { t, language, setLanguage } = useAppSettings();
  const { login } = useAuth();
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await login(email, password);
      navigate("/dashboard");
    } catch (err) {
      const detail =
        err?.response?.data?.detail ||
        err?.message ||
        "Login failed. Please try again.";
      setError(detail);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900 px-4">
      <div className="w-full max-w-md bg-white dark:bg-gray-800 rounded-xl shadow p-6">
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-xl font-bold text-gray-900 dark:text-white">
            {t("welcomeBack")}
          </h1>
          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            className="text-sm border rounded px-2 py-1 bg-transparent dark:text-white"
          >
            {SUPPORTED_LANGUAGES.map((l) => (
              <option key={l.code} value={l.code}>
                {l.label}
              </option>
            ))}
          </select>
        </div>

        {error && (
          <div className="mb-3 text-sm text-red-600 bg-red-50 dark:bg-red-900/30 rounded p-2">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm mb-1 text-gray-700 dark:text-gray-200">
              {t("email")}
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full border rounded px-3 py-2 bg-transparent dark:text-white"
            />
          </div>

          <div>
            <label className="block text-sm mb-1 text-gray-700 dark:text-gray-200">
              {t("password")}
            </label>
            <div className="relative">
              <input
                type={showPassword ? "text" : "password"}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                className="w-full border rounded px-3 py-2 pr-10 bg-transparent dark:text-white"
              />
              <button
                type="button"
                onClick={() => setShowPassword((s) => !s)}
                className="absolute right-2 top-1/2 -translate-y-1/2 text-gray-500 dark:text-gray-300 hover:text-gray-700 dark:hover:text-white"
                aria-label={showPassword ? "Hide password" : "Show password"}
              >
                {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
              </button>
            </div>
          </div>

          <div className="text-right -mt-2">
            <Link
              to="/forgot-password"
              className="text-sm text-blue-600 dark:text-blue-400 hover:underline"
            >
              Forgot password?
            </Link>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 hover:bg-blue-700 disabled:opacity-60 text-white rounded py-2 font-medium"
          >
            {loading ? "..." : t("login")}
          </button>
        </form>

        <p className="mt-4 text-sm text-center text-gray-600 dark:text-gray-300">
          {t("createAccount")}{" "}
          <Link to="/register" className="text-blue-600 dark:text-blue-400">
            {t("register")}
          </Link>
        </p>
      </div>
    </div>
  );
}
