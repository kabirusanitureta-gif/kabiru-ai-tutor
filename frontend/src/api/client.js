import axios from "axios";

// Base URL of the FastAPI backend. Override with VITE_API_URL env var if needed.
export const API_BASE_URL = import.meta.env.VITE_API_URL,

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

function clearSession() {
  localStorage.removeItem("kabiru_token");
  localStorage.removeItem("kabiru_refresh_token");
  localStorage.removeItem("kabiru_user");
}

// Ensures only one /api/auth/refresh call is in flight at a time, even if
// several requests 401 at once — everyone waits on the same promise instead
// of racing to rotate the refresh token multiple times.
let refreshPromise = null;

function performRefresh() {
  const refreshToken = localStorage.getItem("kabiru_refresh_token");
  if (!refreshToken) return Promise.reject(new Error("No refresh token"));

  if (!refreshPromise) {
    // Plain axios call (not the `api` instance) so this request never
    // recurses back through the 401-handling interceptor below.
    refreshPromise = axios
      .post(`${API_BASE_URL}/api/auth/refresh`, { refresh_token: refreshToken })
      .then((res) => {
        localStorage.setItem("kabiru_token", res.data.access_token);
        if (res.data.refresh_token) {
          localStorage.setItem("kabiru_refresh_token", res.data.refresh_token);
        }
        return res.data.access_token;
      })
      .finally(() => {
        refreshPromise = null;
      });
  }
  return refreshPromise;
}

// On a 401, try exactly once to silently refresh the access token and
// replay the original request. If refresh also fails (or there's no
// refresh token — e.g. an older stored session), fall back to the old
// behavior: clear everything so the app redirects to login.
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const original = error.config;
    const isAuthEndpoint = original?.url?.includes("/api/auth/login") || original?.url?.includes("/api/auth/refresh");

    if (error.response && error.response.status === 401 && !original?._retry && !isAuthEndpoint) {
      original._retry = true;
      try {
        const newAccessToken = await performRefresh();
        original.headers.Authorization = `Bearer ${newAccessToken}`;
        return api(original);
      } catch {
        clearSession();
        return Promise.reject(error);
      }
    }

    if (error.response && error.response.status === 401) {
      clearSession();
    }
    return Promise.reject(error);
  }
);

export default api;
