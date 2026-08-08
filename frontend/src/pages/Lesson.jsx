import React, { useEffect, useState } from "react";
import { useParams, Link, useNavigate } from "react-router-dom";
import Layout from "../components/Layout.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";
import { getLesson, completeLesson, checkCode, getQuizzesForLesson } from "../api/endpoints.js";

const SECTION_KEYS = [
  "explanation",
  "examples",
  "practice",
  "mini_project",
  "real_world_project",
  "common_mistakes",
  "best_practices",
  "interview_questions",
  "assignment",
  "challenge",
  "summary",
  "lesson_references",
  "next_lesson_preview",
];
const SECTION_LABELS = {
  explanation: "explanation",
  examples: "examples",
  practice: "practice",
  mini_project: "miniProject",
  real_world_project: "realWorldProject",
  common_mistakes: "commonMistakes",
  best_practices: "bestPractices",
  interview_questions: "interviewQuestions",
  assignment: "assignment",
  challenge: "challenge",
  summary: "summary",
  lesson_references: "references",
  next_lesson_preview: "nextLessonPreview",
};

export default function Lesson() {
  const { lessonId } = useParams();
  const { t } = useAppSettings();
  const navigate = useNavigate();

  const [lesson, setLesson] = useState(null);
  const [quizzes, setQuizzes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [completing, setCompleting] = useState(false);
  const [completed, setCompleted] = useState(false);

  const [code, setCode] = useState("");
  const [checkResult, setCheckResult] = useState(null);
  const [checking, setChecking] = useState(false);

  useEffect(() => {
    let isMounted = true;
    setLoading(true);
    setCheckResult(null);
    setCode("");

    Promise.all([getLesson(lessonId), getQuizzesForLesson(lessonId)])
      .then(([lessonRes, quizRes]) => {
        if (!isMounted) return;
        setLesson(lessonRes.data);
        setQuizzes(quizRes.data);
        // Resume correctly: reflect what the server already has saved for
        // this user instead of forgetting it every time the lesson opens.
        setCompleted(Boolean(lessonRes.data.is_completed));
      })
      .catch((err) => {
        if (!isMounted) return;
        if (err?.response?.status === 403) {
          setError(
            err.response.data?.detail ||
              "This lesson is locked. Complete the previous lesson and pass its quiz first."
          );
        } else {
          setError("Could not load this lesson.");
        }
      })
      .finally(() => isMounted && setLoading(false));

    return () => {
      isMounted = false;
    };
  }, [lessonId]);

  const handleComplete = async () => {
    setCompleting(true);
    try {
      await completeLesson(lessonId);
      setCompleted(true);
    } catch (err) {
      setError("Could not mark this lesson complete.");
    } finally {
      setCompleting(false);
    }
  };

  const handleCheckCode = async () => {
    if (!code.trim()) return;
    setChecking(true);
    setCheckResult(null);
    try {
      const res = await checkCode(code);
      setCheckResult(res.data);
    } catch (err) {
      setCheckResult({
        passed_basic_checks: false,
        feedback_en: "Could not reach the code checker service.",
        feedback_ha: "Ba a iya isa ga sabis din duba code ba.",
        errors: [],
      });
    } finally {
      setChecking(false);
    }
  };

  return (
    <Layout>
      {loading ? (
        <div className="animate-pulse space-y-3">
          <div className="h-8 w-1/2 bg-slate-200 dark:bg-slate-800 rounded" />
          <div className="h-40 bg-slate-200 dark:bg-slate-800 rounded-2xl" />
        </div>
      ) : error ? (
        <div className="text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-3 rounded-xl">
          {error}
        </div>
      ) : (
        lesson && (
          <>
            <button onClick={() => navigate(-1)} className="text-sm text-brand-600 hover:underline">
              ← Back
            </button>
            <div className="flex items-center justify-between mt-2 flex-wrap gap-3">
              <h1 className="text-2xl font-bold">{lesson.title}</h1>
              <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300">
                {lesson.level}
              </span>
            </div>

            <div className="mt-6 space-y-5">
              {SECTION_KEYS.filter((key) => (lesson[key] || "").trim().length > 0).map((key) => (
                <div key={key} className="card">
                  <h2 className="font-bold text-brand-600 uppercase text-xs tracking-wide mb-2">
                    {t(SECTION_LABELS[key])}
                  </h2>
                  {key === "examples" ? (
                    <pre className="bg-slate-900 text-slate-100 rounded-xl p-4 text-sm overflow-x-auto whitespace-pre-wrap">
                      <code>{lesson[key]}</code>
                    </pre>
                  ) : (
                    <p className="text-sm whitespace-pre-line leading-relaxed">{lesson[key]}</p>
                  )}
                </div>
              ))}

              {/* Code checker */}
              <div className="card">
                <h2 className="font-bold text-brand-600 uppercase text-xs tracking-wide mb-2">
                  {t("checkMyCode")}
                </h2>
                <textarea
                  value={code}
                  onChange={(e) => setCode(e.target.value)}
                  placeholder={t("yourCode")}
                  rows={8}
                  className="input-field font-mono text-sm"
                  spellCheck={false}
                />
                <button onClick={handleCheckCode} disabled={checking} className="btn-primary mt-3 text-sm">
                  {checking ? "..." : t("checkMyCode")}
                </button>

                {checkResult && (
                  <div
                    className={`mt-4 rounded-xl p-4 text-sm ${
                      checkResult.passed_basic_checks
                        ? "bg-emerald-50 dark:bg-emerald-900/20 text-emerald-700 dark:text-emerald-400"
                        : "bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400"
                    }`}
                  >
                    <p className="font-semibold mb-1">🇬🇧 English</p>
                    <p className="whitespace-pre-line">{checkResult.feedback_en}</p>
                    <p className="font-semibold mt-3 mb-1">🇳🇬 Hausa</p>
                    <p className="whitespace-pre-line">{checkResult.feedback_ha}</p>
                  </div>
                )}
              </div>
            </div>

            <div className="mt-6 flex flex-wrap gap-3">
              <button
                onClick={handleComplete}
                disabled={completing || completed}
                className="btn-primary"
              >
                {completed ? "✓ Completed" : completing ? "..." : t("completeLesson")}
              </button>

              {quizzes.length > 0 && (
                <Link to={`/quizzes/${quizzes[0].id}`} className="btn-secondary">
                  {t("takeQuiz")}
                </Link>
              )}
            </div>
          </>
        )
      )}
    </Layout>
  );
}
