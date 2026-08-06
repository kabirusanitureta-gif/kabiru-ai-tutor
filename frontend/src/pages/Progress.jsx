import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Layout from "../components/Layout.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";
import { getDashboard, getMyAttempts } from "../api/endpoints.js";

export default function Progress() {
  const { t } = useAppSettings();
  const [dashboard, setDashboard] = useState(null);
  const [attempts, setAttempts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let isMounted = true;
    Promise.all([getDashboard(), getMyAttempts()])
      .then(([dashRes, attemptsRes]) => {
        if (!isMounted) return;
        setDashboard(dashRes.data);
        setAttempts(attemptsRes.data);
      })
      .catch(() => isMounted && setError("Could not load your progress."))
      .finally(() => isMounted && setLoading(false));
    return () => {
      isMounted = false;
    };
  }, []);

  return (
    <Layout>
      <h1 className="text-2xl font-bold">{t("yourProgress")}</h1>
      <p className="text-slate-500 dark:text-slate-400 mt-1">
        Track how far you've come across every course.
      </p>

      {error && (
        <div className="mt-6 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-3 rounded-xl">
          {error}
        </div>
      )}

      {loading ? (
        <div className="mt-6 animate-pulse space-y-4">
          <div className="h-32 bg-slate-200 dark:bg-slate-800 rounded-2xl" />
          <div className="h-64 bg-slate-200 dark:bg-slate-800 rounded-2xl" />
        </div>
      ) : (
        dashboard && (
          <>
            <div className="card mt-6">
              <div className="flex items-center justify-between mb-2">
                <h2 className="font-bold">Overall Completion</h2>
                <span className="font-extrabold text-brand-600 text-lg">
                  {dashboard.overall_percent}%
                </span>
              </div>
              <div className="h-3 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                <div
                  className="h-full bg-brand-600 rounded-full transition-all"
                  style={{ width: `${dashboard.overall_percent}%` }}
                />
              </div>
              <p className="text-sm text-slate-500 dark:text-slate-400 mt-2">
                {dashboard.total_completed_lessons} of {dashboard.total_lessons} lessons completed
                &nbsp;•&nbsp; 🔥 {dashboard.current_streak} day streak (best: {dashboard.longest_streak})
              </p>
            </div>

            <h2 className="text-lg font-bold mt-8 mb-3">Progress by Course</h2>
            <div className="space-y-3">
              {dashboard.courses.map((c) => (
                <Link key={c.course_slug} to={`/courses/${c.course_slug}`} className="card block hover:shadow-md transition-shadow">
                  <div className="flex items-center justify-between mb-2">
                    <h3 className="font-semibold">{c.course_title}</h3>
                    <span className="text-sm font-semibold text-brand-600">{c.percent_complete}%</span>
                  </div>
                  <div className="h-2 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-brand-600 rounded-full transition-all"
                      style={{ width: `${c.percent_complete}%` }}
                    />
                  </div>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-1.5">
                    {c.completed_lessons}/{c.total_lessons} lessons
                  </p>
                </Link>
              ))}
            </div>

            <h2 className="text-lg font-bold mt-8 mb-3">Recent Quiz Attempts</h2>
            <div className="card overflow-x-auto">
              {attempts.length === 0 ? (
                <p className="text-sm text-slate-500 dark:text-slate-400">No quiz attempts yet.</p>
              ) : (
                <table className="w-full text-sm">
                  <thead>
                    <tr className="text-left text-slate-500 dark:text-slate-400 border-b border-slate-200 dark:border-slate-700">
                      <th className="py-2 pr-4">Score</th>
                      <th className="py-2 pr-4">Result</th>
                      <th className="py-2">Date</th>
                    </tr>
                  </thead>
                  <tbody>
                    {attempts.map((a) => (
                      <tr key={a.id} className="border-b border-slate-100 dark:border-slate-800 last:border-0">
                        <td className="py-2 pr-4 font-semibold">{a.score_percent}%</td>
                        <td className="py-2 pr-4">
                          {a.passed ? (
                            <span className="text-emerald-600 dark:text-emerald-400 font-semibold">Passed</span>
                          ) : (
                            <span className="text-red-500 font-semibold">Failed</span>
                          )}
                        </td>
                        <td className="py-2 text-slate-500 dark:text-slate-400">
                          {new Date(a.created_at).toLocaleDateString()}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>
          </>
        )
      )}
    </Layout>
  );
}
