import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import Layout from "../components/Layout.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";
import { getCourse, getMyProgress, issueCertificate } from "../api/endpoints.js";

const LEVEL_COLORS = {
  beginner: "bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400",
  intermediate: "bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400",
  advanced: "bg-rose-100 text-rose-700 dark:bg-rose-900/30 dark:text-rose-400",
};

export default function CourseDetail() {
  const { slug } = useParams();
  const { t } = useAppSettings();

  const [course, setCourse] = useState(null);
  const [progressMap, setProgressMap] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [certMessage, setCertMessage] = useState("");

  useEffect(() => {
    let isMounted = true;
    setLoading(true);
    Promise.all([getCourse(slug), getMyProgress()])
      .then(([courseRes, progressRes]) => {
        if (!isMounted) return;
        setCourse(courseRes.data);
        const map = {};
        progressRes.data.forEach((p) => {
          map[p.lesson_id] = p;
        });
        setProgressMap(map);
      })
      .catch(() => isMounted && setError("Could not load this course."))
      .finally(() => isMounted && setLoading(false));
    return () => {
      isMounted = false;
    };
  }, [slug]);

  const completedCount = course
    ? course.lessons.filter((l) => progressMap[l.id]?.completed).length
    : 0;
  const allCompleted = course && course.lessons.length > 0 && completedCount === course.lessons.length;

  const handleGetCertificate = async () => {
    setCertMessage("");
    try {
      await issueCertificate(slug);
      setCertMessage("🎉 Certificate issued! View it on the Certificates page.");
    } catch (err) {
      setCertMessage(err?.response?.data?.detail || "Could not issue certificate yet.");
    }
  };

  return (
    <Layout>
      {loading ? (
        <div className="animate-pulse space-y-3">
          <div className="h-8 w-1/2 bg-slate-200 dark:bg-slate-800 rounded" />
          <div className="h-24 bg-slate-200 dark:bg-slate-800 rounded-2xl" />
        </div>
      ) : error ? (
        <div className="text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-3 rounded-xl">
          {error}
        </div>
      ) : (
        course && (
          <>
            <Link to="/courses" className="text-sm text-brand-600 hover:underline">
              ← {t("courses")}
            </Link>
            <h1 className="text-2xl font-bold mt-2">{course.title}</h1>
            <p className="text-slate-500 dark:text-slate-400 mt-1">{course.description}</p>

            <div className="mt-4 flex items-center gap-3">
              <div className="flex-1 h-2 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden max-w-xs">
                <div
                  className="h-full bg-brand-600 rounded-full"
                  style={{
                    width: `${course.lessons.length ? (completedCount / course.lessons.length) * 100 : 0}%`,
                  }}
                />
              </div>
              <span className="text-sm text-slate-500 dark:text-slate-400">
                {completedCount}/{course.lessons.length}
              </span>
            </div>

            {allCompleted && (
              <div className="card mt-4 bg-brand-50 dark:bg-brand-900/20 border-brand-200 dark:border-brand-800">
                <p className="font-semibold">🎉 You've completed this course!</p>
                <button onClick={handleGetCertificate} className="btn-primary mt-3 text-sm">
                  {t("viewCertificate")}
                </button>
                {certMessage && <p className="text-sm mt-2">{certMessage}</p>}
              </div>
            )}

            <div className="mt-6 space-y-2">
              {course.lessons.map((lesson, idx) => {
                const done = progressMap[lesson.id]?.completed;
                const locked = lesson.locked;
                const content = (
                  <>
                    <div className="flex items-center gap-3">
                      <div
                        className={`h-8 w-8 rounded-full flex items-center justify-center text-sm font-bold ${
                          done
                            ? "bg-brand-600 text-white"
                            : locked
                            ? "bg-slate-100 dark:bg-slate-800 text-slate-400 dark:text-slate-500"
                            : "bg-slate-100 dark:bg-slate-700 text-slate-500 dark:text-slate-300"
                        }`}
                      >
                        {done ? "✓" : locked ? "🔒" : idx + 1}
                      </div>
                      <div>
                        <div className={`font-medium ${locked ? "text-slate-400 dark:text-slate-500" : ""}`}>
                          {lesson.title}
                        </div>
                        <span
                          className={`inline-block mt-1 text-xs font-semibold px-2 py-0.5 rounded-full ${
                            LEVEL_COLORS[lesson.level] || LEVEL_COLORS.beginner
                          }`}
                        >
                          {lesson.level}
                        </span>
                      </div>
                    </div>
                    <span className="text-slate-400">{locked ? "" : "→"}</span>
                  </>
                );

                return locked ? (
                  <div
                    key={lesson.id}
                    title={t("lessonLockedHint") || "Complete the previous lesson and pass its quiz to unlock this one."}
                    className="card flex items-center justify-between opacity-60 cursor-not-allowed select-none"
                  >
                    {content}
                  </div>
                ) : (
                  <Link
                    key={lesson.id}
                    to={`/lessons/${lesson.id}`}
                    className="card flex items-center justify-between hover:shadow-md transition-shadow"
                  >
                    {content}
                  </Link>
                );
              })}
              {course.lessons.length === 0 && (
                <p className="text-sm text-slate-500 dark:text-slate-400">
                  Lessons for this course are coming soon.
                </p>
              )}
            </div>
          </>
        )
      )}
    </Layout>
  );
}
