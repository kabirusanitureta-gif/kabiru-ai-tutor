import api from "./client.js";

// ---- Auth ----
export const registerUser = (payload) => api.post("/api/auth/register", payload);
export const loginUser = (payload) => api.post("/api/auth/login-json", payload);
export const getMe = () => api.get("/api/auth/me");
export const updateMe = (payload) => api.patch("/api/auth/me", payload);

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
