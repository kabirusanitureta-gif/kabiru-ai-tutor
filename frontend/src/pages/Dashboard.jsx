import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Layout from "../components/Layout.jsx";
import { useAuth } from "../context/AuthContext.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";
import { getDashboard, getNextLesson, pingStreak } from "../api/endpoints.js";

export default function Dashboard() {
  const { user } = useAuth();
  const { t } = useAppSettings();

  const [dashboard, setDashboard] = useState(null);
  const [nextLesson, setNextLesson] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let isMounted = true;

    async function load() {
      try {
        await pingStreak(); // record today's activity
        const [dashRes, nextRes] = await Promise.all([getDashboard(), getNextLesson()]);
        if (isMounted) {
          setDashboard(dashRes.data);
          setNextLesson(nextRes.data);
        }
      } catch (err) {
        if (isMounted) setError("Could not load your dashboard. Please check your connection to the backend.");
      } finally {
        if (isMounted) setLoading(false);
      }
    }

    load();
    return () => {
      isMounted = false;
    };
  }, []);

  return (
    <Layout>
      <h1 className="text-2xl font-bold">
        {t("welcomeBack")}, {user?.full_name?.split(" ")[0] || "there"} 👋
      </h1>
      <p className="text-slate-500 dark:text-slate-400 mt-1">Here's where you left off.</p>

      {error && (
        <div className="mt-6 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-3 rounded-xl">
          {error}
        </div>
      )}

      {loading ? (
        <div className="mt-8 animate-pulse space-y-4">
          <div className="h-24 bg-slate-200 dark:bg-slate-800 rounded-2xl" />
          <div className="h-40 bg-slate-200 dark:bg-slate-800 rounded-2xl" />
        </div>
      ) : (
        dashboard && (
          <>
            {/* Top stats */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6">
              <div className="card text-center">
                <div className="text-3xl font-extrabold text-brand-600">
                  {dashboard.overall_percent}%
                </div>
                <div className="text-xs text-slate-500 dark:text-slate-400 mt-1">Overall Progress</div>
              </div>
              <div className="card text-center">
                <div className="text-3xl font-extrabold text-brand-600">
                  {dashboard.total_completed_lessons}/{dashboard.total_lessons}
                </div>
                <div className="text-xs text-slate-500 dark:text-slate-400 mt-1">Lessons Completed</div>
              </div>
              <div className="card text-center">
                <div className="text-3xl font-extrabold text-brand-600">🔥 {dashboard.current_streak}</div>
                <div className="text-xs text-slate-500 dark:text-slate-400 mt-1">{t("streak")}</div>
              </div>
              <div className="card text-center">
                <div className="text-3xl font-extrabold text-brand-600">{dashboard.longest_streak}</div>
                <div className="text-xs text-slate-500 dark:text-slate-400 mt-1">Longest Streak</div>
              </div>
            </div>

            {/* Next lesson recommendation */}
            {nextLesson && nextLesson.lesson_id ? (
              <div className="card mt-6 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                <div>
                  <div className="text-xs font-semibold text-brand-600 uppercase tracking-wide">
                    {nextLesson.course_title}
                  </div>
                  <h2 className="text-lg font-bold mt-1">{nextLesson.lesson_title}</h2>
                  <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">{nextLesson.reason}</p>
                </div>
                <Link to={`/lessons/${nextLesson.lesson_id}`} className="btn-primary text-center whitespace-nowrap">
                  {t("continueLearning")}
                </Link>
              </div>
            ) : (
              <div className="card mt-6 text-center py-8">
                <p className="font-semibold">🎉 You've completed all available lessons!</p>
              </div>
            )}

            {/* Per-course progress */}
            <h2 className="text-lg font-bold mt-8 mb-3">{t("yourProgress")}</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {dashboard.courses.map((c) => (
                <Link key={c.course_slug} to={`/courses/${c.course_slug}`} className="card hover:shadow-md transition-shadow">
                  <div className="flex items-center justify-between">
                    <h3 className="font-semibold">{c.course_title}</h3>
                    <span className="text-sm text-slate-500 dark:text-slate-400">
                      {c.completed_lessons}/{c.total_lessons}
                    </span>
                  </div>
                  <div className="mt-3 h-2 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-brand-600 rounded-full transition-all"
                      style={{ width: `${c.percent_complete}%` }}
                    />
                  </div>
                </Link>
              ))}
            </div>
          </>
        )
      )}
    </Layout>
  );
}
