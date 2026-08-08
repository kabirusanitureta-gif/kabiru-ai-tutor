import api from "./client.js";

// ---- Auth ----
export const registerUser = (payload) => api.post("/api/auth/register", payload);
export const loginUser = (payload) => api.post("/api/auth/login-json", payload);
export const getMe = () => api.get("/api/auth/me");
export const updateMe = (payload) => api.patch("/api/auth/me", payload);
export const uploadMyPhoto = (file) => {
  const formData = new FormData();
  formData.append("file", file);
  return api.post("/api/auth/me/photo", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};
export const deleteMyPhoto = () => api.delete("/api/auth/me/photo");
// avatar_url from the API is a relative path (e.g. "/uploads/avatars/xyz.jpg");
// prefix with the API base so <img src> works regardless of frontend origin.
export const avatarSrc = (avatar_url) => (avatar_url ? `${api.defaults.baseURL}${avatar_url}` : null);

// ---- Admin ----
export const getAuditLogs = (params = {}) => api.get("/api/admin/audit-logs", { params });
export const getDashboardStats = () => api.get("/api/admin/dashboard");
export const listAdminUsers = (params = {}) => api.get("/api/admin/users", { params });
export const changeUserRole = (userId, role) =>
  api.patch(`/api/admin/users/${userId}/role`, null, { params: { role } });
export const toggleUserActive = (userId) => api.patch(`/api/admin/users/${userId}/toggle-active`);
export const softDeleteUser = (userId) => api.delete(`/api/admin/users/${userId}`);
export const restoreUser = (userId) => api.post(`/api/admin/users/${userId}/restore`);
export const listRoles = () => api.get("/api/admin/roles");
export const listPermissionsCatalog = () => api.get("/api/admin/permissions");
export const setRolePermission = (role, permission, allowed) =>
  api.put(`/api/admin/permissions/${role}/${permission}`, null, { params: { allowed } });
export const logoutUser = (refresh_token) => api.post("/api/auth/logout", { refresh_token });
export const forgotPassword = (email) => api.post("/api/auth/forgot-password", { email });
export const resetPassword = (email, code, new_password) =>
  api.post("/api/auth/reset-password", { email, code, new_password });
export const verifyEmail = (email, pin) => api.post("/api/auth/verify-email", { email, pin });
export const resendVerification = (email) => api.post("/api/auth/resend-verification", { email });

// ---- WebAuthn (Face ID / Touch ID / Windows Hello passkeys) ----
export const webauthnRegisterOptions = () => api.post("/api/auth/webauthn/register/options");
export const webauthnRegisterVerify = (state_id, credential, device_name) =>
  api.post("/api/auth/webauthn/register/verify", { state_id, credential, device_name });
export const webauthnLoginOptions = (email) => api.post("/api/auth/webauthn/login/options", { email });
export const webauthnLoginVerify = (state_id, credential) =>
  api.post("/api/auth/webauthn/login/verify", { state_id, credential });
export const listMyPasskeys = () => api.get("/api/auth/webauthn/credentials");
export const renamePasskey = (id, device_name) => api.patch(`/api/auth/webauthn/credentials/${id}`, { device_name });
export const deletePasskey = (id) => api.delete(`/api/auth/webauthn/credentials/${id}`);

// ---- Courses ----
export const getCourses = () => api.get("/api/courses");
export const getCourse = (slug) => api.get(`/api/courses/${slug}`);

// ---- Lessons ----
export const getLesson = (lessonId) => api.get(`/api/lessons/${lessonId}`);
export const searchLessons = (q) => api.get(`/api/lessons/search`, { params: { q } });
export const completeLesson = (lessonId) => api.post(`/api/lessons/${lessonId}/complete`);
export const getNextLesson = () => api.get(`/api/lessons/recommend/next`);

// ---- Quizzes ----
export const getQuizzesForLesson = (lessonId) => api.get(`/api/quizzes/lesson/${lessonId}`);
export const getQuiz = (quizId) => api.get(`/api/quizzes/${quizId}`);
export const submitQuiz = (quizId, answers) => api.post(`/api/quizzes/${quizId}/submit`, { answers });
export const getMyAttempts = () => api.get(`/api/quizzes/attempts/mine`);

// ---- Progress ----
export const getDashboard = () => api.get(`/api/progress/dashboard`);
export const getMyProgress = () => api.get(`/api/progress/mine`);
export const pingStreak = () => api.post(`/api/progress/streak/ping`);

// ---- Notes ----
export const getNotes = () => api.get(`/api/notes`);
export const createNote = (payload) => api.post(`/api/notes`, payload);
export const updateNote = (noteId, payload) => api.put(`/api/notes/${noteId}`, payload);
export const deleteNote = (noteId) => api.delete(`/api/notes/${noteId}`);

// ---- Certificates ----
export const getCertificates = () => api.get(`/api/certificates`);
export const issueCertificate = (courseSlug) => api.post(`/api/certificates/issue/${courseSlug}`);
export const certificateDownloadUrl = (certId) => `${api.defaults.baseURL}/api/certificates/${certId}/download`;

// ---- Chat / AI Tutor ----
export const sendChatMessage = (message) => api.post(`/api/chat`, { message });
export const getChatHistory = () => api.get(`/api/chat/history`);
export const explainError = (message) => api.post(`/api/chat/explain-error`, { message });
export const checkCode = (code, language = "python", task_description = "") =>
  api.post(`/api/chat/check-code`, { code, language, task_description });
