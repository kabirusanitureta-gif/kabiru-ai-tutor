import React from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { Sun, Moon } from "lucide-react";
import { useAppSettings, SUPPORTED_LANGUAGES } from "../context/AppSettingsContext";

const NAV_ITEMS = [
  { to: "/dashboard", key: "dashboard" },
  { to: "/courses", key: "courses" },
  { to: "/ai-chat", key: "aiChat" },
  { to: "/progress", key: "progress" },
  { to: "/certificates", key: "certificates" },
  { to: "/notes", key: "notes" },
  { to: "/settings", key: "settings" },
];

export default function Layout({ children }) {
  const { t, language, setLanguage, theme, toggleTheme } = useAppSettings();
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("kabiru_token");
    navigate("/login");
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <header className="bg-white dark:bg-gray-800 shadow px-4 py-3 flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-4">
          <span className="font-bold text-gray-900 dark:text-white">
            {t("appName")}
          </span>
          <nav className="hidden md:flex items-center gap-3">
            {NAV_ITEMS.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                className={({ isActive }) =>
                  `text-sm px-2 py-1 rounded ${
                    isActive
                      ? "bg-blue-600 text-white"
                      : "text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                  }`
                }
              >
                {t(item.key)}
              </NavLink>
            ))}
          </nav>
        </div>

        <div className="flex items-center gap-3">
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

          <button
            onClick={toggleTheme}
            className="p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-600 dark:text-gray-300"
            aria-label={theme === "dark" ? t("lightMode") : t("darkMode")}
          >
            {theme === "dark" ? <Sun size={18} /> : <Moon size={18} />}
          </button>

          <button
            onClick={handleLogout}
            className="text-sm text-red-600 dark:text-red-400 hover:underline"
          >
            {t("logout")}
          </button>
        </div>
      </header>

      {/* Mobile nav */}
      <nav className="md:hidden flex overflow-x-auto gap-2 px-4 py-2 bg-white dark:bg-gray-800 border-t dark:border-gray-700">
        {NAV_ITEMS.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            className={({ isActive }) =>
              `text-xs whitespace-nowrap px-2 py-1 rounded ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
              }`
            }
          >
            {t(item.key)}
          </NavLink>
        ))}
      </nav>

      <main>{children}</main>
    </div>
  );
}
