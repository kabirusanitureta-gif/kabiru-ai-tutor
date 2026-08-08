import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import Layout from "../components/Layout.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";
import { getQuiz, submitQuiz } from "../api/endpoints.js";

const OPTION_KEYS = ["a", "b", "c", "d"];

export default function Quiz() {
  const { quizId } = useParams();
  const { t } = useAppSettings();
  const navigate = useNavigate();

  const [quiz, setQuiz] = useState(null);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState(null);

  useEffect(() => {
    let isMounted = true;
    setLoading(true);
    setResult(null);
    setAnswers({});

    getQuiz(quizId)
      .then((res) => {
        if (!isMounted) return;
        setQuiz(res.data);
        // Resume correctly: if this quiz was already passed before, show
        // that instead of a blank form that looks like progress was lost.
        if (res.data.quiz_passed) {
          setResult({
            score_percent: res.data.best_score_percent ?? res.data.passing_score,
            passed: true,
            already_passed: true,
          });
        }
      })
      .catch(() => isMounted && setError("Could not load this quiz."))
      .finally(() => isMounted && setLoading(false));

    return () => {
      isMounted = false;
    };
  }, [quizId]);

  const selectAnswer = (questionId, optionKey) => {
    setAnswers((prev) => ({ ...prev, [questionId]: optionKey }));
  };

  const handleSubmit = async () => {
    setSubmitting(true);
    setError("");
    try {
      const res = await submitQuiz(quizId, answers);
      setResult(res.data);
    } catch (err) {
      setError(err?.response?.data?.detail || "Could not submit the quiz.");
    } finally {
      setSubmitting(false);
    }
  };

  const allAnswered = quiz && quiz.questions.every((q) => answers[q.id]);

  return (
    <Layout>
      {loading ? (
        <div className="animate-pulse space-y-3">
          <div className="h-8 w-1/2 bg-slate-200 dark:bg-slate-800 rounded" />
          <div className="h-40 bg-slate-200 dark:bg-slate-800 rounded-2xl" />
        </div>
      ) : error && !quiz ? (
        <div className="text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-3 rounded-xl">
          {error}
        </div>
      ) : (
        quiz && (
          <>
            <button onClick={() => navigate(-1)} className="text-sm text-brand-600 hover:underline">
              ← Back
            </button>
            <h1 className="text-2xl font-bold mt-2">{quiz.title}</h1>
            <p className="text-slate-500 dark:text-slate-400 mt-1">
              Passing score: {quiz.passing_score}%
            </p>

            {result ? (
              <div
                className={`card mt-6 text-center ${
                  result.passed
                    ? "bg-emerald-50 dark:bg-emerald-900/20"
                    : "bg-red-50 dark:bg-red-900/20"
                }`}
              >
                <div className="text-4xl font-extrabold">{result.score_percent}%</div>
                <p className="mt-2 font-semibold">
                  {result.already_passed
                    ? "✓ You already passed this quiz"
                    : result.passed
                    ? "🎉 You passed!"
                    : "Not quite — try again!"}
                </p>
                <div className="mt-4 flex justify-center gap-3">
                  <button onClick={() => navigate(-1)} className="btn-secondary">
                    Back to Lesson
                  </button>
                  {(!result.passed || result.already_passed) && (
                    <button
                      onClick={() => {
                        setResult(null);
                        setAnswers({});
                      }}
                      className="btn-primary"
                    >
                      Retake Quiz
                    </button>
                  )}
                </div>
              </div>
            ) : (
              <>
                <div className="mt-6 space-y-5">
                  {quiz.questions.map((question, idx) => (
                    <div key={question.id} className="card">
                      <p className="font-semibold mb-3">
                        {idx + 1}. {question.text}
                      </p>
                      <div className="space-y-2">
                        {OPTION_KEYS.map((key) => {
                          const optionText = question[`option_${key}`];
                          const selected = answers[question.id] === key;
                          return (
                            <button
                              key={key}
                              onClick={() => selectAnswer(question.id, key)}
                              className={`w-full text-left px-4 py-2.5 rounded-xl text-sm border transition-colors ${
                                selected
                                  ? "border-brand-600 bg-brand-50 dark:bg-brand-900/20 font-semibold"
                                  : "border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700/50"
                              }`}
                            >
                              <span className="uppercase text-xs font-bold mr-2 text-slate-400">
                                {key}
                              </span>
                              {optionText}
                            </button>
                          );
                        })}
                      </div>
                    </div>
                  ))}
                </div>

                {error && (
                  <div className="mt-4 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-3 rounded-xl">
                    {error}
                  </div>
                )}

                <button
                  onClick={handleSubmit}
                  disabled={!allAnswered || submitting}
                  className="btn-primary mt-6"
                >
                  {submitting ? "..." : t("submitQuiz")}
                </button>
              </>
            )}
          </>
        )
      )}
    </Layout>
  );
}
