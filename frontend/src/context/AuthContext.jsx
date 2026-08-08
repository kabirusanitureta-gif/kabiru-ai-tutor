import React, { createContext, useContext, useState, useEffect } from "react";
import { startAuthentication, startRegistration, browserSupportsWebAuthn } from "@simplewebauthn/browser";
import {
  loginUser,
  registerUser,
  getMe,
  logoutUser,
  webauthnRegisterOptions,
  webauthnRegisterVerify,
  webauthnLoginOptions,
  webauthnLoginVerify,
} from "../api/endpoints.js";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    const stored = localStorage.getItem("kabiru_user");
    return stored ? JSON.parse(stored) : null;
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("kabiru_token");
    if (!token) {
      setLoading(false);
      return;
    }
    // Validate the stored token by fetching the current user's fresh profile.
    getMe()
      .then((res) => {
        setUser(res.data);
        localStorage.setItem("kabiru_user", JSON.stringify(res.data));
      })
      .catch(() => {
        localStorage.removeItem("kabiru_token");
        localStorage.removeItem("kabiru_user");
        setUser(null);
      })
      .finally(() => setLoading(false));
  }, []);

  const login = async (email, password) => {
    const res = await loginUser({ email, password });
    localStorage.setItem("kabiru_token", res.data.access_token);
    if (res.data.refresh_token) {
      localStorage.setItem("kabiru_refresh_token", res.data.refresh_token);
    }
    localStorage.setItem("kabiru_user", JSON.stringify(res.data.user));
    setUser(res.data.user);
    return res.data.user;
  };

  const register = async (full_name, email, password, preferred_language) => {
    const res = await registerUser({ full_name, email, password, preferred_language });
    localStorage.setItem("kabiru_token", res.data.access_token);
    if (res.data.refresh_token) {
      localStorage.setItem("kabiru_refresh_token", res.data.refresh_token);
    }
    localStorage.setItem("kabiru_user", JSON.stringify(res.data.user));
    setUser(res.data.user);
    return res.data.user;
  };

  const _applySession = (data) => {
    localStorage.setItem("kabiru_token", data.access_token);
    if (data.refresh_token) {
      localStorage.setItem("kabiru_refresh_token", data.refresh_token);
    }
    localStorage.setItem("kabiru_user", JSON.stringify(data.user));
    setUser(data.user);
    return data.user;
  };

  // Sign in with Face ID / Touch ID / Windows Hello / a security key,
  // instead of a password. `email` is optional — omit it to let the
  // authenticator's own account picker (e.g. Face ID) choose the passkey.
  const loginWithPasskey = async (email) => {
    const { data: opts } = await webauthnLoginOptions(email || undefined);
    const credential = await startAuthentication({ optionsJSON: opts.options });
    const res = await webauthnLoginVerify(opts.state_id, credential);
    return _applySession(res.data);
  };

  // Register the current device's biometric authenticator (Face ID / Touch
  // ID / Windows Hello) as a passkey for the already-logged-in user.
  const registerPasskey = async (deviceName) => {
    const { data: opts } = await webauthnRegisterOptions();
    const credential = await startRegistration({ optionsJSON: opts.options });
    const res = await webauthnRegisterVerify(opts.state_id, credential, deviceName);
    return res.data;
  };

  const logout = () => {
    const refreshToken = localStorage.getItem("kabiru_refresh_token");
    // Best-effort: revoke the refresh token server-side so it can't be
    // replayed later. Don't block the UI logout on this succeeding.
    if (refreshToken) {
      logoutUser(refreshToken).catch(() => {});
    }
    localStorage.removeItem("kabiru_token");
    localStorage.removeItem("kabiru_refresh_token");
    localStorage.removeItem("kabiru_user");
    setUser(null);
  };

  const updateLocalUser = (updatedUser) => {
    setUser(updatedUser);
    localStorage.setItem("kabiru_user", JSON.stringify(updatedUser));
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        login,
        register,
        logout,
        updateLocalUser,
        isAuthenticated: !!user,
        loginWithPasskey,
        registerPasskey,
        webauthnSupported: browserSupportsWebAuthn(),
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}
