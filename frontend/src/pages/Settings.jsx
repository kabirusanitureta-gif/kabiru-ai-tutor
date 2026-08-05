import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout.jsx";
import { useAuth } from "../context/AuthContext.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";
import { updateMe, searchLessons } from "../api/endpoints.js";

export default function Settings() {
  const { user, updateLocalUser } = useAuth();
  const { theme, toggleTheme, language, setLanguage, t } = useAppSettings();
  const navigate = useNavigate();

  const [fullName, setFullName] = useState(user?.full_name || "");
  const [saving, setSaving] = useState(false);
  const [saveMessage, setSaveMessage] = useState("");

  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [searching, setSearching] = useState(false);

  const handleSaveProfile = async (e) => {
    e.preventDefault();
    setSaving(true);
    setSaveMessage("");
    try {
      const res = await updateMe({ full_name: fullName, preferred_language: language });
      updateLocalUser(res.data);
      setSaveMessage("Saved!");
    } catch (err) {
      setSaveMessage("Could not save changes.");
    } finally {
      setSaving(false);
      setTimeout(() => setSaveMessage(""), 2500);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;
    setSearching(true);
    try {
      const res = await searchLessons(query.trim());
      setResults(res.data);
    } catch (err) {
      setResults([]);
    } finally {
      setSearching(false);
    }
  };

  return (
    <Layout>
      <h1 className="text-2xl font-bold">{t("settings")}</h1>

      {/* Profile */}
      <div className="card mt-6">
        <h2 className="font-bold mb-4">Profile</h2>
        <form onSubmit={handleSaveProfile} className="space-y-4 max-w-sm">
          <div>
            <label className="block text-sm font-medium mb-1">{t("fullName")}</label>
            <input
              type="text"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              className="input-field"
              minLength={2}
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">{t("email")}</label>
            <input type="email" value={user?.email || ""} disabled className="input-field opacity-60" />
          </div>
          <button type="submit" disabled={saving} className="btn-primary">
            {saving ? "..." : t("save")}
          </button>
          {saveMessage && <span className="ml-3 text-sm text-brand-600">{saveMessage}</span>}
        </form>
      </div>

      {/* Preferences */}
      <div className="card mt-6">
        <h2 className="font-bold mb-4">Preferences</h2>
        <div className="flex flex-wrap gap-6">
          <div>
            <label className="block text-sm font-medium mb-2">Theme</label>
            <button onClick={toggleTheme} className="btn-secondary text-sm">
              {theme === "dark" ? `☀️ ${t("lightMode")}` : `🌙 ${t("darkMode")}`}
            </button>
          </div>
          <div>
            <label className="block text-sm font-medium mb-2">{t("language")}</label>
            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
              className="input-field"
            >
              <option value="en">English</option>
              <option value="ha">Hausa</option>
            </select>
          </div>
        </div>
      </div>

      {/* Search lessons */}
      <div className="card mt-6">
        <h2 className="font-bold mb-4">{t("searchLessons")}</h2>
        <form onSubmit={handleSearch} className="flex gap-2 max-w-md">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder={t("searchLessons")}
            className="input-field"
          />
          <button type="submit" disabled={searching} className="btn-primary whitespace-nowrap">
            {searching ? "..." : "🔍"}
          </button>
        </form>

        {results.length > 0 && (
          <div className="mt-4 space-y-2">
            {results.map((lesson) => (
              <button
                key={lesson.id}
                onClick={() => navigate(`/lessons/${lesson.id}`)}
                className="w-full text-left px-4 py-2.5 rounded-xl text-sm border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700/50"
              >
                {lesson.title}
              </button>
            ))}
          </div>
        )}
      </div>
    </Layout>
  );
}
