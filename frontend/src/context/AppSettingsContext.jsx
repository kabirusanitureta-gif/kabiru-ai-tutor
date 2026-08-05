import React, { createContext, useContext, useState, useEffect } from "react";

const AppSettingsContext = createContext(null);

// Compact bilingual dictionary for UI strings. Keys are used across all pages.
const TRANSLATIONS = {
  en: {
    appName: "Kabiru AI Tutor",
    dashboard: "Dashboard",
    courses: "Courses",
    aiChat: "AI Chat",
    progress: "Progress",
    certificates: "Certificates",
    notes: "Notes",
    settings: "Settings",
    login: "Login",
    register: "Register",
    logout: "Logout",
    email: "Email",
    password: "Password",
    fullName: "Full Name",
    welcomeBack: "Welcome back",
    createAccount: "Create your account",
    continueLearning: "Continue Learning",
    yourProgress: "Your Progress",
    streak: "Day Streak",
    searchLessons: "Search lessons...",
    startLesson: "Start Lesson",
    completeLesson: "Mark as Complete",
    takeQuiz: "Take Quiz",
    submitQuiz: "Submit Quiz",
    explanation: "Explanation",
    examples: "Examples",
    practice: "Practice",
    miniProject: "Mini Project",
    realWorldProject: "Real-World Project",
    commonMistakes: "Common Mistakes",
    bestPractices: "Best Practices",
    interviewQuestions: "Interview Questions",
    assignment: "Assignment",
    challenge: "Challenge",
    summary: "Summary",
    references: "References",
    nextLessonPreview: "Next Lesson Preview",
    askTutor: "Ask your AI tutor anything...",
    send: "Send",
    darkMode: "Dark Mode",
    lightMode: "Light Mode",
    language: "Language",
    getStarted: "Get Started",
    viewCertificate: "View Certificate",
    download: "Download",
    save: "Save",
    cancel: "Cancel",
    delete: "Delete",
    newNote: "New Note",
    noNotesYet: "No notes yet. Start writing!",
    checkMyCode: "Check My Code",
    yourCode: "Your Code (Python)",
    lessonLockedHint: "Complete the previous lesson and pass its quiz to unlock this one.",
  },
  ha: {
    appName: "Kabiru AI Tutor",
    dashboard: "Dashboard",
    courses: "Darussa",
    aiChat: "Tattaunawa da AI",
    progress: "Ci gaba",
    certificates: "Takardun shaida",
    notes: "Bayanai",
    settings: "Saitunan",
    login: "Shiga",
    register: "Yi rijista",
    logout: "Fita",
    email: "Imel",
    password: "Kalmar sirri",
    fullName: "Cikakken suna",
    welcomeBack: "Barka da dawowa",
    createAccount: "Kirkiri asusun ka",
    continueLearning: "Ci gaba da koyo",
    yourProgress: "Ci gabanka",
    streak: "Kwanaki a jere",
    searchLessons: "Nemo darasi...",
    startLesson: "Fara Darasi",
    completeLesson: "Kammala Darasi",
    takeQuiz: "Yi Jarrabawa",
    submitQuiz: "Mika Jarrabawa",
    explanation: "Bayani",
    examples: "Misalai",
    practice: "Aiki",
    miniProject: "Karamin Aiki",
    realWorldProject: "Aiki na Zahiri",
    commonMistakes: "Kurakurai na Kowa",
    bestPractices: "Hanyoyin da Suka Fi Dacewa",
    interviewQuestions: "Tambayoyin Hira",
    assignment: "Aikin Gida",
    challenge: "Kalubale",
    summary: "Takaitawa",
    references: "Ambato",
    nextLessonPreview: "Gabatarwar Darasi Na Gaba",
    askTutor: "Tambayi malamin AI naka...",
    send: "Aika",
    darkMode: "Duhu",
    lightMode: "Haske",
    language: "Harshe",
    getStarted: "Fara",
    viewCertificate: "Duba Takardar shaida",
    download: "Sauke",
    save: "Ajiye",
    cancel: "Soke",
    delete: "Goge",
    newNote: "Sabon Bayani",
    noNotesYet: "Babu bayani tukuna. Fara rubutu!",
    checkMyCode: "Duba Code Dina",
    yourCode: "Code Dinka (Python)",
    lessonLockedHint: "Kammala darasi na baya kuma ka ci jarabawarsa kafin ka bude wannan.",
  },
};

export function AppSettingsProvider({ children }) {
  const [theme, setTheme] = useState(() => localStorage.getItem("kabiru_theme") || "light");
  const [language, setLanguage] = useState(() => localStorage.getItem("kabiru_language") || "en");

  useEffect(() => {
    const root = document.documentElement;
    if (theme === "dark") {
      root.classList.add("dark");
    } else {
      root.classList.remove("dark");
    }
    localStorage.setItem("kabiru_theme", theme);
  }, [theme]);

  useEffect(() => {
    localStorage.setItem("kabiru_language", language);
  }, [language]);

  const toggleTheme = () => setTheme((t) => (t === "dark" ? "light" : "dark"));
  const toggleLanguage = () => setLanguage((l) => (l === "en" ? "ha" : "en"));

  const t = (key) => TRANSLATIONS[language]?.[key] ?? TRANSLATIONS.en[key] ?? key;

  return (
    <AppSettingsContext.Provider
      value={{ theme, setTheme, toggleTheme, language, setLanguage, toggleLanguage, t }}
    >
      {children}
    </AppSettingsContext.Provider>
  );
}

export function useAppSettings() {
  const ctx = useContext(AppSettingsContext);
  if (!ctx) throw new Error("useAppSettings must be used within AppSettingsProvider");
  return ctx;
}
