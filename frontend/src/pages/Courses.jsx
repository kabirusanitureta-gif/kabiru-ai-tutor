import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Layout from "../components/Layout.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";
import { getCourses } from "../api/endpoints.js";

const COURSE_ICONS = {
  python: "🐍",
  sqlite: "🗄️",
  fastapi: "⚡",
  linux: "🐧",
  git: "🔧",
  "web-development": "🌐",
  "ai-fundamentals": "🤖",
  "electronics-arduino": "🔌",
  "electrical-engineering": "🔋",
};

export default function Courses() {
  const { t } = useAppSettings();
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    getCourses()
      .then((res) => setCourses(res.data))
      .catch(() => setError("Could not load courses. Please check your connection to the backend."))
      .finally(() => setLoading(false));
  }, []);

  return (
    <Layout>
      <h1 className="text-2xl font-bold">{t("courses")}</h1>
      <p className="text-slate-500 dark:text-slate-400 mt-1">
        Pick a course to continue — from beginner to expert.
      </p>

      {error && (
        <div className="mt-6 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-3 rounded-xl">
          {error}
        </div>
      )}

      {loading ? (
        <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 gap-4 animate-pulse">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="h-32 bg-slate-200 dark:bg-slate-800 rounded-2xl" />
          ))}
        </div>
      ) : (
        <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 gap-4">
          {courses.map((course) => (
            <Link key={course.slug} to={`/courses/${course.slug}`} className="card hover:shadow-md transition-shadow">
              <div className="text-3xl">{COURSE_ICONS[course.slug] || "📘"}</div>
              <h3 className="font-bold text-lg mt-2">{course.title}</h3>
              <p className="text-sm text-slate-500 dark:text-slate-400 mt-1 line-clamp-3">
                {course.description}
              </p>
              <div className="mt-3 text-xs font-semibold text-brand-600">
                {course.lessons.length} {course.lessons.length === 1 ? "lesson" : "lessons"}
              </div>
            </Link>
          ))}
        </div>
      )}
    </Layout>
  );
}
