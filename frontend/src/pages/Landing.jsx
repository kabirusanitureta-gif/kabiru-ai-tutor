import React from "react";
import { Link } from "react-router-dom";
import { useAppSettings } from "../context/AppSettingsContext.jsx";

const FEATURES = [
  { icon: "🐍", title: "Python", desc: "30 lessons from variables to a final CLI capstone project." },
  { icon: "🗄️", title: "SQLite", desc: "10 lessons on databases, queries, joins, and transactions." },
  { icon: "⚡", title: "FastAPI", desc: "15 lessons building real, secured, tested REST APIs." },
  { icon: "🐧", title: "Linux", desc: "10 lessons mastering the terminal and shell scripting." },
  { icon: "🔧", title: "Git & GitHub", desc: "5 lessons on version control and collaboration." },
  { icon: "🤖", title: "AI Tutor", desc: "Ask questions anytime — answered in Hausa or English." },
];

export default function Landing() {
  const { t, language, toggleLanguage, theme, toggleTheme } = useAppSettings();

  return (
    <div className="min-h-screen bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100">
      <header className="flex items-center justify-between px-6 py-4 max-w-6xl mx-auto">
        <div className="flex items-center gap-2 font-bold text-xl">
          <span className="text-brand-600">🎓</span>
          <span>{t("appName")}</span>
        </div>
        <div className="flex items-center gap-3">
          <button onClick={toggleLanguage} className="text-sm px-3 py-1.5 rounded-lg border border-slate-300 dark:border-slate-600">
            {language === "en" ? "Hausa" : "English"}
          </button>
          <button onClick={toggleTheme} className="text-sm px-3 py-1.5 rounded-lg border border-slate-300 dark:border-slate-600">
            {theme === "dark" ? "☀️" : "🌙"}
          </button>
          <Link to="/login" className="btn-secondary text-sm !py-1.5 !px-4">{t("login")}</Link>
        </div>
      </header>

      <section className="px-6 py-16 md:py-24 max-w-4xl mx-auto text-center">
        <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight">
          Learn to code with your own
          <span className="text-brand-600"> personal AI tutor</span>
        </h1>
        <p className="mt-6 text-lg text-slate-600 dark:text-slate-300 max-w-2xl mx-auto">
          Kabiru AI Tutor takes you from complete beginner to expert in Python, SQLite, FastAPI, Linux,
          and Git & GitHub — with quizzes, coding exercises, progress tracking, certificates, and an AI
          tutor that explains things in simple Hausa or English. Works fully offline.
        </p>
        <div className="mt-8 flex flex-wrap items-center justify-center gap-4">
          <Link to="/register" className="btn-primary text-base">{t("getStarted")}</Link>
          <Link to="/login" className="btn-secondary text-base">{t("login")}</Link>
        </div>
      </section>

      <section className="px-6 pb-24 max-w-6xl mx-auto">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {FEATURES.map((f) => (
            <div key={f.title} className="card">
              <div className="text-3xl">{f.icon}</div>
              <h3 className="mt-3 font-bold text-lg">{f.title}</h3>
              <p className="mt-1 text-sm text-slate-600 dark:text-slate-300">{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      <footer className="px-6 py-8 text-center text-sm text-slate-500 dark:text-slate-400 border-t border-slate-200 dark:border-slate-800">
        Built for Kabiru Sani — Nigeria 🇳🇬. Runs offline on Termux, Pydroid, Linux, and Windows.
      </footer>
    </div>
  );
}
