import React, { useState, useEffect, useCallback } from "react";
import { useNavigate, Link } from "react-router-dom";
import Layout from "../components/Layout.jsx";
import { useAuth } from "../context/AuthContext.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";
import {
  updateMe,
  searchLessons,
  uploadMyPhoto,
  deleteMyPhoto,
  avatarSrc,
  listMyPasskeys,
  deletePasskey,
} from "../api/endpoints.js";

function PasskeySettings() {
  const { registerPasskey, webauthnSupported } = useAuth();
  const [passkeys, setPasskeys] = useState([]);
  const [loadingList, setLoadingList] = useState(true);
  const [adding, setAdding] = useState(false);
  const [message, setMessage] = useState("");

  const refresh = useCallback(() => {
    listMyPasskeys()
      .then((res) => setPasskeys(res.data))
      .catch(() => setPasskeys([]))
      .finally(() => setLoadingList(false));
  }, []);

  useEffect(() => {
    refresh();
  }, [refresh]);

  const handleAdd = async () => {
    setMessage("");
    setAdding(true);
    try {
      await registerPasskey();
      setMessage("Face ID / Touch ID enabled on this device!");
      refresh();
    } catch (err) {
      if (err?.name !== "NotAllowedError") {
        setMessage(err?.response?.data?.detail || "Could not set up Face ID / Touch ID on this device.");
      }
    } finally {
      setAdding(false);
      setTimeout(() => setMessage(""), 4000);
    }
  };

  const handleRemove = async (id) => {
    try {
      await deletePasskey(id);
      setPasskeys((prev) => prev.filter((p) => p.id !== id));
    } catch (err) {
      setMessage("Could not remove that passkey.");
      setTimeout(() => setMessage(""), 3000);
    }
  };

  if (!webauthnSupported) return null;

  return (
    <div className="card mt-6">
      <h2 className="font-bold mb-1">Face ID / Biometric Login</h2>
      <p className="text-sm text-slate-500 dark:text-slate-400 mb-4">
        Sign in instantly using this device's Face ID, Touch ID, or Windows Hello — no password needed.
        Your biometric data never leaves your device or reaches our servers.
      </p>

      {!loadingList && passkeys.length > 0 && (
        <div className="space-y-2 mb-4">
          {passkeys.map((pk) => (
            <div
              key={pk.id}
              className="flex items-center justify-between px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 text-sm"
            >
              <div>
                <div className="font-medium">{pk.device_name || "Passkey"}</div>
                <div className="text-xs text-slate-400">
                  Added {new Date(pk.created_at).toLocaleDateString()}
                  {pk.last_used_at ? ` · last used ${new Date(pk.last_used_at).toLocaleDateString()}` : ""}
                </div>
              </div>
              <button onClick={() => handleRemove(pk.id)} className="text-red-500 hover:underline text-xs">
                Remove
              </button>
            </div>
          ))}
        </div>
      )}

      <button onClick={handleAdd} disabled={adding} className="btn-secondary text-sm">
        {adding ? "..." : "🆔 Set up Face ID / Touch ID on this device"}
      </button>
      {message && <div className="text-sm text-brand-600 mt-2">{message}</div>}
    </div>
  );
}

export default function Settings() {
  const { user, updateLocalUser } = useAuth();
  const { theme, toggleTheme, language, setLanguage, t } = useAppSettings();
  const navigate = useNavigate();

  const [fullName, setFullName] = useState(user?.full_name || "");
  const [saving, setSaving] = useState(false);
  const [saveMessage, setSaveMessage] = useState("");

  const [photoBusy, setPhotoBusy] = useState(false);
  const [photoMessage, setPhotoMessage] = useState("");

  const handlePhotoChange = async (e) => {
    const file = e.target.files?.[0];
    e.target.value = ""; // allow re-selecting the same file later
    if (!file) return;
    setPhotoBusy(true);
    setPhotoMessage("");
    try {
      const res = await uploadMyPhoto(file);
      updateLocalUser(res.data);
      setPhotoMessage("Photo updated!");
    } catch (err) {
      setPhotoMessage(err?.response?.data?.detail || "Could not upload photo.");
    } finally {
      setPhotoBusy(false);
      setTimeout(() => setPhotoMessage(""), 3000);
    }
  };

  const handleRemovePhoto = async () => {
    setPhotoBusy(true);
    setPhotoMessage("");
    try {
      const res = await deleteMyPhoto();
      updateLocalUser(res.data);
      setPhotoMessage("Photo removed.");
    } catch (err) {
      setPhotoMessage("Could not remove photo.");
    } finally {
      setPhotoBusy(false);
      setTimeout(() => setPhotoMessage(""), 3000);
    }
  };

  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [searching, setSearching] = useState(false);

  const handleSaveProfile = async (e) => {
    e.preventDefault();
    const trimmedName = fullName.trim().replace(/\s+/g, " ");
    if (trimmedName.length < 2) {
      setSaveMessage("Please enter your full name.");
      setTimeout(() => setSaveMessage(""), 2500);
      return;
    }
    setSaving(true);
    setSaveMessage("");
    try {
      const res = await updateMe({ full_name: trimmedName, preferred_language: language });
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

        <div className="flex items-center gap-4 mb-6">
          <div className="w-16 h-16 rounded-full overflow-hidden bg-slate-200 dark:bg-slate-700 flex items-center justify-center text-xl font-bold text-slate-500">
            {user?.avatar_url ? (
              <img src={avatarSrc(user.avatar_url)} alt="Profile" className="w-full h-full object-cover" />
            ) : (
              (user?.full_name || "?").charAt(0).toUpperCase()
            )}
          </div>
          <div>
            <label className="btn-secondary text-sm cursor-pointer inline-block">
              {photoBusy ? "..." : "Change photo"}
              <input
                type="file"
                accept="image/jpeg,image/png,image/webp"
                onChange={handlePhotoChange}
                disabled={photoBusy}
                className="hidden"
              />
            </label>
            {user?.avatar_url && (
              <button onClick={handleRemovePhoto} disabled={photoBusy} className="ml-2 text-sm text-red-500 hover:underline">
                Remove
              </button>
            )}
            {photoMessage && <div className="text-sm text-brand-600 mt-1">{photoMessage}</div>}
          </div>
        </div>

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

      {/* Security */}
      <div className="card mt-6">
        <h2 className="font-bold mb-1">Security</h2>
        <p className="text-sm text-slate-500 dark:text-slate-400 mb-4">
          Change your password, or sign in with Face ID / Touch ID instead — see below.
        </p>
        <Link to="/forgot-password" className="btn-secondary text-sm inline-block">
          Change password
        </Link>
        <p className="text-xs text-slate-400 mt-2">
          We'll email you a reset code — the same flow as "Forgot password" on the login screen.
        </p>
      </div>

      <PasskeySettings />

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
