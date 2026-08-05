import React, { createContext, useContext, useState, useEffect } from "react";
import { loginUser, registerUser, getMe } from "../api/endpoints.js";

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
    localStorage.setItem("kabiru_user", JSON.stringify(res.data.user));
    setUser(res.data.user);
    return res.data.user;
  };

  const register = async (full_name, email, password, preferred_language) => {
    const res = await registerUser({ full_name, email, password, preferred_language });
    localStorage.setItem("kabiru_token", res.data.access_token);
    localStorage.setItem("kabiru_user", JSON.stringify(res.data.user));
    setUser(res.data.user);
    return res.data.user;
  };

  const logout = () => {
    localStorage.removeItem("kabiru_token");
    localStorage.removeItem("kabiru_user");
    setUser(null);
  };

  const updateLocalUser = (updatedUser) => {
    setUser(updatedUser);
    localStorage.setItem("kabiru_user", JSON.stringify(updatedUser));
  };

  return (
    <AuthContext.Provider
      value={{ user, loading, login, register, logout, updateLocalUser, isAuthenticated: !!user }}
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
