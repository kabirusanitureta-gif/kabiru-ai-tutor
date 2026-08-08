# Free AI API Research for Kabiru AI Tutor

Verified against each provider's official docs/pricing pages, August 2026.
Goal: $0 forever, no credit card, permanent (not a trial), works from
FastAPI on Render.

## Classification of every provider investigated

| Provider | Status | Why |
|---|---|---|
| **Groq** | ✅ PERMANENT FREE TIER | No card, no expiry. Rate-limited (RPM/TPM/RPD), not a shrinking credit balance. |
| **Cloudflare Workers AI** | ✅ PERMANENT FREE TIER | 10,000 Neurons/day, resets daily forever, per official pricing docs. No card for the free allocation. |
| **SambaNova Cloud** | ✅ PERMANENT FREE TIER (thinner) | Official docs: "Free Tier: Applied when there is no payment method linked." Genuinely ongoing, but low RPD on some models. |
| **Google AI Studio (Gemini)** | ✅ PERMANENT FREE TIER | Excluded — you asked not to depend on Gemini. |
| **Mistral (La Plateforme)** | ⚠️ PERMANENT but eval-only | Free "Experiment" tier, no card, no published expiry — but Mistral's own docs mark it for evaluation, not production. |
| **Cohere** | ⚠️ PERMANENT but eval-only | Trial key never expires (1,000 calls/month) but Cohere's ToS explicitly forbid production/commercial use on it. |
| **Cerebras** | ⚠️ PERMANENT but volatile | No card, but published limits and the free model catalog have changed several times in 2026 — plan for it to shift under you. |
| **OpenRouter** | ⚠️ FREE TRIAL-ish / volatile | No card needed, `:free` models exist — but the free model list rotates weekly/monthly with no warning; models get delisted. Not safe to hard-code. |
| **Hugging Face Inference Providers** | ❌ NOT ACTUALLY FREE | Free tier gives under $0.10/month in inference credit — not enough for real chat traffic. The Hub itself (browsing models) is free, but that's not an API for your tutor. |
| **Together AI** | ❌ NOT ACTUALLY FREE | Official docs (2026): no free trial anymore; $5 minimum credit purchase required to use the API at all. |
| **Fireworks AI** | ❌ NOT ACTUALLY FREE | $1 one-time signup credit, then postpaid. Requires a card to lift the 10 RPM cap. |

## Can any provider "suddenly charge money without activating billing"?

No, for the providers above marked ✅ or ⚠️ — Groq, Cloudflare, SambaNova,
Mistral, and Cohere all only start charging once **you** explicitly add a
payment method. Until then, exceeding the free rate limit just returns an
HTTP 429 error (rejected request) — it never becomes a bill. This is
standard behavior for all of them per their own docs. The only way to be
charged $0.001 you didn't expect is to voluntarily add a card.

## Top 5 ranked for Kabiru AI Tutor

1. **Groq** — fastest, genuinely permanent, no card, real production-grade
   open models (Llama 3.3 70B, GPT-OSS 120B), OpenAI-compatible endpoint
   (drop-in for FastAPI/httpx), officially documented rate limits.
2. **Cloudflare Workers AI** — most generous "no catch" free allocation
   (10,000 Neurons/day, forever), but Neurons-per-request varies by model
   so daily conversation capacity is less predictable than Groq's RPD.
3. **SambaNova Cloud** — good backup, official permanent free tier, but
   thinner published limits (as low as 20 RPD on some models — verify the
   current model's limit before relying on it).
4. **Mistral La Plateforme** — fine for development/testing, but Mistral's
   own docs say the free tier is not meant for production traffic.
5. **Cerebras** — very fast, technically permanent and card-free, but the
   free model catalog has narrowed and shifted multiple times in 2026; use
   only if you can tolerate occasionally updating the model name.

## #1 Recommendation: Groq

- **Why**: only provider that is simultaneously (a) officially permanent,
  (b) no credit card, (c) real production-capable models, (d) an
  OpenAI-compatible REST API (zero new SDK — `httpx` already in the
  project works), and (e) fast enough that a student on Render's free
  plan doesn't feel the extra network hop.
- Official docs: <https://console.groq.com/docs/rate-limits>,
  <https://groq.com/pricing>
- Published free-tier limits (subject to Groq updating them — always
  check `console.groq.com/docs/rate-limits` for the current numbers):
  roughly **30 requests/minute, ~6,000–12,000 tokens/minute, and
  ~1,000–14,400 requests/day** depending on model. `llama-3.3-70b-versatile`
  is a solid general tutoring model within these limits.
- Hausa support: no LLM provider publishes an explicit Hausa benchmark,
  but Llama 3.3 70B (and GPT-OSS 120B, also on Groq) handle Hausa
  noticeably better than smaller 7–8B models because of broader
  multilingual pretraining data. Test with real Kabiru prompts and keep
  the rule-based Hausa fallback as a safety net either way.

## #2 Backup: Cloudflare Workers AI

Different infrastructure entirely (Cloudflare's edge GPUs vs Groq's LPUs),
so an outage or a sudden Groq rate-limit change won't take down both at
once. Official pricing: <https://developers.cloudflare.com/workers-ai/platform/pricing/>.
10,000 Neurons/day, no card, resets at 00:00 UTC. Swapping to it only
means changing `AI_API_BASE_URL`, `AI_API_KEY`, and `AI_API_MODEL` — the
code in `ai_tutor.py` already speaks the OpenAI-compatible chat-completions
shape both providers use.

## Is self-hosting the only way to get *truly* unlimited free usage?

Yes — every hosted API, including Groq, is rate-limited by design; "free"
here means "free while inside published limits," not "unlimited." The
only genuinely unlimited option is self-hosting an open-weight model
(e.g. via Ollama, like this project's local-dev fallback already does),
which trades $0 API cost for needing your own GPU/CPU capacity — not
practical on Render's free web-service plan. For Kabiru AI Tutor's scale
(a small educational project), Groq's free tier is the practical $0
solution; self-hosting is the fallback if you ever outgrow it and still
don't want to pay per token.

## Final decision

**Primary: Groq. Backup: Cloudflare Workers AI.** Both are wired into
`backend/app/services/ai_tutor.py` as drop-in-compatible via
`AI_API_BASE_URL` / `AI_API_KEY` / `AI_API_MODEL`, sitting between the
local Ollama tier (dev only) and the always-available rule-based tutor.
