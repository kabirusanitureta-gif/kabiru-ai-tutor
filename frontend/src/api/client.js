import axios from "axios";

// Base URL of the FastAPI backend. Override with VITE_API_URL env var if needed.
export const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const api = axios.create({
  baseURL: API_BASE_URL,
});

// Attach the JWT token (if present) to every outgoing request.
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("kabiru_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// If the token is invalid/expired, clear it so the app can redirect to login.
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem("kabiru_token");
      localStorage.removeItem("kabiru_user");
    }
    return Promise.reject(error);
  }
);

export default api;
