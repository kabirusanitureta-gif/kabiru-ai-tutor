import React, { useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";

const NAV_ITEMS = [
  { to: "/dashboard", key: "dashboard", icon: "🏠" },
  { to: "/courses", key: "courses", icon: "📚" },
  { to: "/chat", key: "aiChat", icon: "💬" },
  { to: "/progress", key: "progress", icon: "📈" },
  { to: "/certificates", key: "certificates", icon: "🎓" },
  { to: "/notes", key: "notes", icon: "📝" },
];

export default function Layout({ children }) {
  const { user, logout } = useAuth();
  const { theme, toggleTheme, language, toggleLanguage, t } = useAppSettings();
  const navigate = useNavigate();
  const [menuOpen, setMenuOpen] = useState(false);

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900 text-slate-900 dark:text-slate-100 flex flex-col md:flex-row">
      {/* Sidebar (desktop) / Top bar (mobile) */}
      <aside className="md:w-64 md:min-h-screen bg-white dark:bg-slate-800 border-b md:border-b-0 md:border-r border-slate-200 dark:border-slate-700 flex md:flex-col">
        <div className="flex items-center justify-between w-full p-4 md:border-b border-slate-200 dark:border-slate-700">
          <NavLink to="/dashboard" className="flex items-center gap-2 font-bold text-lg">
            <span className="text-brand-600">🎓</span>
            <span>{t("appName")}</span>
          </NavLink>
          <button
            className="md:hidden text-2xl"
            onClick={() => setMenuOpen((o) => !o)}
            aria-label="Toggle menu"
          >
            ☰
          </button>
        </div>

        <nav
          className={`${menuOpen ? "flex" : "hidden"} md:flex flex-col gap-1 p-3 md:flex-1 absolute md:static top-16 left-0 right-0 bg-white dark:bg-slate-800 z-20 md:z-auto border-b md:border-b-0 border-slate-200 dark:border-slate-700`}
        >
          {NAV_ITEMS.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              onClick={() => setMenuOpen(false)}
              className={({ isActive }) =>
                `flex items-center gap-3 px-4 py-2.5 rounded-xl text-sm font-medium transition-colors ${
                  isActive
                    ? "bg-brand-600 text-white"
                    : "hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200"
                }`
              }
            >
              <span>{item.icon}</span>
              <span>{t(item.key)}</span>
            </NavLink>
          ))}

          <div className="mt-2 border-t border-slate-200 dark:border-slate-700 pt-2 flex flex-col gap-1">
            {user && ["super_admin", "admin", "moderator", "teacher"].includes(user.role) && (
              <NavLink
                to="/admin"
                onClick={() => setMenuOpen(false)}
                className={({ isActive }) =>
                  `flex items-center gap-3 px-4 py-2.5 rounded-xl text-sm font-medium transition-colors ${
                    isActive
                      ? "bg-brand-600 text-white"
                      : "hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200"
                  }`
                }
              >
                <span>🛡️</span>
                <span>Admin</span>
              </NavLink>
            )}
            <NavLink
              to="/settings"
              onClick={() => setMenuOpen(false)}
              className={({ isActive }) =>
                `flex items-center gap-3 px-4 py-2.5 rounded-xl text-sm font-medium transition-colors ${
                  isActive
                    ? "bg-brand-600 text-white"
                    : "hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200"
                }`
              }
            >
              <span>⚙️</span>
              <span>{t("settings")}</span>
            </NavLink>

            <button
              onClick={toggleTheme}
              className="flex items-center gap-3 px-4 py-2.5 rounded-xl text-sm font-medium hover:bg-slate-100 dark:hover:bg-slate-700 text-left"
            >
              <span>{theme === "dark" ? "☀️" : "🌙"}</span>
              <span>{theme === "dark" ? t("lightMode") : t("darkMode")}</span>
            </button>

            <button
              onClick={toggleLanguage}
              className="flex items-center gap-3 px-4 py-2.5 rounded-xl text-sm font-medium hover:bg-slate-100 dark:hover:bg-slate-700 text-left"
            >
              <span>🌐</span>
              <span>{language === "en" ? "Hausa" : "English"}</span>
            </button>

            <button
              onClick={handleLogout}
              className="flex items-center gap-3 px-4 py-2.5 rounded-xl text-sm font-medium text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20 text-left"
            >
              <span>🚪</span>
              <span>{t("logout")}</span>
            </button>
          </div>
        </nav>

        {user && (
          <div className="hidden md:flex items-center gap-3 p-4 border-t border-slate-200 dark:border-slate-700">
            <div className="h-9 w-9 rounded-full bg-brand-600 text-white flex items-center justify-center font-bold">
              {user.full_name?.[0]?.toUpperCase() || "K"}
            </div>
            <div className="text-sm">
              <div className="font-semibold leading-tight">{user.full_name}</div>
              <div className="text-slate-500 dark:text-slate-400 text-xs leading-tight">{user.email}</div>
            </div>
          </div>
        )}
      </aside>

      <main className="flex-1 p-4 md:p-8 max-w-6xl w-full mx-auto">{children}</main>
    </div>
  );
}
