import React, { useEffect, useRef, useState } from "react";
import Layout from "../components/Layout.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";
import { sendChatMessage, getChatHistory } from "../api/endpoints.js";

export default function Chat() {
  const { t } = useAppSettings();
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(true);
  const [sending, setSending] = useState(false);
  const [error, setError] = useState("");
  const bottomRef = useRef(null);

  useEffect(() => {
    getChatHistory()
      .then((res) => {
        setMessages(
          res.data.map((m) => ({ role: m.role, content: m.content, language: m.language }))
        );
      })
      .catch(() => setError("Could not load chat history."))
      .finally(() => setLoading(false));
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, sending]);

  const handleSend = async (e) => {
    e.preventDefault();
    const trimmed = input.trim();
    if (!trimmed || sending) return;

    setMessages((prev) => [...prev, { role: "user", content: trimmed, language: "en" }]);
    setInput("");
    setSending(true);
    setError("");

    try {
      const res = await sendChatMessage(trimmed);
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: res.data.reply, language: res.data.language },
      ]);
    } catch (err) {
      setError("Could not reach the AI tutor. Please try again.");
    } finally {
      setSending(false);
    }
  };

  return (
    <Layout>
      <h1 className="text-2xl font-bold">{t("aiChat")}</h1>
      <p className="text-slate-500 dark:text-slate-400 mt-1">
        Ask anything about Python, SQLite, FastAPI, Linux, or Git — in English or Hausa.
      </p>

      <div className="card mt-6 flex flex-col h-[65vh]">
        <div className="flex-1 overflow-y-auto space-y-3 pr-1">
          {loading ? (
            <div className="animate-pulse space-y-3">
              <div className="h-10 w-2/3 bg-slate-200 dark:bg-slate-700 rounded-2xl" />
              <div className="h-10 w-1/2 bg-slate-200 dark:bg-slate-700 rounded-2xl ml-auto" />
            </div>
          ) : messages.length === 0 ? (
            <div className="h-full flex items-center justify-center text-center text-slate-400 dark:text-slate-500 text-sm px-6">
              👋 Say hello, or ask something like "explain loops" or "menene variable?"
            </div>
          ) : (
            messages.map((m, idx) => (
              <div
                key={idx}
                className={`max-w-[85%] px-4 py-2.5 rounded-2xl text-sm whitespace-pre-line ${
                  m.role === "user"
                    ? "bg-brand-600 text-white ml-auto rounded-br-sm"
                    : "bg-slate-100 dark:bg-slate-700 text-slate-800 dark:text-slate-100 rounded-bl-sm"
                }`}
              >
                {m.content}
              </div>
            ))
          )}
          {sending && (
            <div className="bg-slate-100 dark:bg-slate-700 text-slate-500 dark:text-slate-400 max-w-[60%] px-4 py-2.5 rounded-2xl rounded-bl-sm text-sm">
              <span className="inline-flex gap-1">
                <span className="animate-bounce">●</span>
                <span className="animate-bounce [animation-delay:0.1s]">●</span>
                <span className="animate-bounce [animation-delay:0.2s]">●</span>
              </span>
            </div>
          )}
          <div ref={bottomRef} />
        </div>

        {error && (
          <div className="mt-3 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-2 rounded-xl">
            {error}
          </div>
        )}

        <form onSubmit={handleSend} className="mt-3 flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder={t("askTutor")}
            className="input-field"
          />
          <button type="submit" disabled={sending || !input.trim()} className="btn-primary whitespace-nowrap">
            {t("send")}
          </button>
        </form>
      </div>
    </Layout>
  );
}
