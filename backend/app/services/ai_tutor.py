"""
Kabiru AI Tutor
Provider priority:
1. Google Gemini
2. Ollama
3. Rule-based fallback

Supports:
- Hausa / English
- Conversation history
- Gemini fallback models
- Ollama fallback
- Offline rule-based responses
"""

import httpx

from app.core.config import settings


# ============================================================
# LANGUAGE DETECTION
# ============================================================

HAUSA_MARKERS = {
    "ina", "yaya", "menene", "don", "me", "yasa",
    "wannan", "wancan", "na", "ba", "ne", "ce",
    "ake", "yake", "zan", "zai", "ka", "ki",
    "mu", "ku", "su", "abin", "abu", "yaushe",
    "nawa", "sannu", "godiya", "koyi", "koya",
    "malam", "dalibi", "kuskure", "lambar",
    "shirin", "yaya kake",
}


def detect_language(text: str) -> str:
    lowered = text.lower()

    words = set(
        lowered
        .replace(",", " ")
        .replace(".", " ")
        .replace("?", " ")
        .replace("!", " ")
        .split()
    )

    hits = words.intersection(HAUSA_MARKERS)

    return "ha" if hits else "en"


# ============================================================
# EXPERTISE
# ============================================================

_EXPERT_DOMAINS_EN = (
    "software engineering, Python, FastAPI, SQLite, PostgreSQL, "
    "Linux, Git, GitHub, HTML, CSS, JavaScript, TypeScript, React, "
    "Node.js, Docker, DevOps, networking, cybersecurity basics, "
    "algorithms and data structures, artificial intelligence, "
    "machine learning, electrical engineering, electronics, "
    "embedded systems, Arduino, ESP32, microcontrollers, PCB design, "
    "robotics, automation, IoT, solar energy and hardware engineering"
)

_EXPERT_DOMAINS_HA = (
    "injiniyan software, Python, FastAPI, SQLite, PostgreSQL, "
    "Linux, Git, GitHub, HTML, CSS, JavaScript, TypeScript, React, "
    "Node.js, Docker, DevOps, network, cybersecurity, algorithms, "
    "AI, machine learning, injiniyan lantarki, electronics, "
    "embedded systems, Arduino, ESP32, microcontrollers, PCB, "
    "robotics, automation, IoT, solar energy da hardware"
)


def _build_system_prompt(language: str) -> str:

    if language == "ha":
        return (
            "Kai ne Kabiru AI Tutor. Kai malami ne mai hakuri, "
            "abokantaka kuma kwararre. "
            f"Ka kware a: {_EXPERT_DOMAINS_HA}. "
            "Ka koyar da dalibi daga beginner zuwa advanced. "
            "Ka bayyana abu a hankali kuma cikin sauki. "
            "Idan kana bada code, ka bada code mai aiki sannan ka "
            "yi bayanin yadda yake aiki. "
            "Ka guji kirkirar bayanan karya. "
            "Idan tambayar ba ta da isasshen bayani, ka tambayi "
            "dalibi abin da ya kamata ya kara bayani. "
            "Amsa cikin Hausa kawai."
        )

    return (
        "You are Kabiru AI Tutor, a friendly, patient and highly "
        "knowledgeable teacher. "
        f"You specialize in: {_EXPERT_DOMAINS_EN}. "
        "Teach students from complete beginner to advanced level. "
        "Explain concepts clearly and practically. "
        "When providing code, make it runnable and explain how it works. "
        "Do not invent facts. "
        "If the question lacks important information, ask a concise "
        "clarifying question. "
        "Respond in English only."
    )


# ============================================================
# GEMINI
# ============================================================

_GEMINI_API_BASE = (
    "https://generativelanguage.googleapis.com/v1beta/models"
)


def _build_gemini_contents(
    message: str,
    history: list[dict] | None = None,
) -> list[dict]:

    contents = []

    if history:
        for item in history:

            role = item.get("role")
            content = str(item.get("content", "")).strip()

            if not content:
                continue

            if role == "assistant":
                gemini_role = "model"
            else:
                gemini_role = "user"

            contents.append(
                {
                    "role": gemini_role,
                    "parts": [
                        {
                            "text": content
                        }
                    ],
                }
            )

    contents.append(
        {
            "role": "user",
            "parts": [
                {
                    "text": message
                }
            ],
        }
    )

    return contents


def _ask_gemini(
    prompt: str,
    language: str,
    history: list[dict] | None = None,
) -> str | None:

    api_key = settings.GEMINI_API_KEY

    if not api_key:
        return None

    system_prompt = _build_system_prompt(language)

    payload = {
        "system_instruction": {
            "parts": [
                {
                    "text": system_prompt
                }
            ]
        },
        "contents": _build_gemini_contents(
            prompt,
            history,
        ),
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 2048,
        },
    }

    models = [
        settings.GEMINI_MODEL,
        *settings.gemini_fallback_models_list,
    ]

    tried = set()

    for model in models:

        model = model.strip()

        if not model or model in tried:
            continue

        tried.add(model)

        try:

            response = httpx.post(
                f"{_GEMINI_API_BASE}/{model}:generateContent",
                params={
                    "key": api_key
                },
                json=payload,
                timeout=45.0,
            )

            if response.status_code != 200:
                continue

            data = response.json()

            candidates = data.get(
                "candidates",
                []
            )

            if not candidates:
                continue

            parts = (
                candidates[0]
                .get("content", {})
                .get("parts", [])
            )

            text = "".join(
                part.get("text", "")
                for part in parts
                if isinstance(part, dict)
            ).strip()

            if text:
                return text

        except Exception:
            continue

    return None


# ============================================================
# OLLAMA
# ============================================================

def _list_ollama_models() -> list[str]:

    if not settings.OLLAMA_ENABLED:
        return []

    try:

        response = httpx.get(
            f"{settings.OLLAMA_BASE_URL}/api/tags",
            timeout=3.0,
        )

        if response.status_code != 200:
            return []

        data = response.json()

        return [
            model.get("name", "")
            for model in data.get("models", [])
            if model.get("name")
        ]

    except Exception:
        return []


def _pick_best_model(
    available_models: list[str],
) -> str | None:

    if not available_models:
        return None

    explicit = (
        settings.OLLAMA_MODEL
        .strip()
        .lower()
    )

    if explicit and explicit != "auto":

        for model in available_models:

            if model.lower() == explicit:
                return model

    for family in settings.ollama_preferred_models_list:

        for model in available_models:

            if family.lower() in model.lower():
                return model

    return available_models[0]


def _ollama_available() -> tuple[bool, str | None]:

    models = _list_ollama_models()

    model = _pick_best_model(models)

    return model is not None, model


def _ask_ollama(
    prompt: str,
    language: str,
    model: str,
    history: list[dict] | None = None,
) -> str | None:

    system_prompt = _build_system_prompt(language)

    conversation = ""

    if history:

        for item in history:

            role = item.get("role", "user")
            content = str(
                item.get("content", "")
            ).strip()

            if content:

                conversation += (
                    f"{role}: {content}\n"
                )

    conversation += f"user: {prompt}\nassistant:"

    try:

        response = httpx.post(
            f"{settings.OLLAMA_BASE_URL}/api/generate",
            json={
                "model": model,
                "system": system_prompt,
                "prompt": conversation,
                "stream": False,
            },
            timeout=60.0,
        )

        if response.status_code == 200:

            data = response.json()

            text = data.get(
                "response",
                ""
            ).strip()

            if text:
                return text

    except Exception:
        pass

    return None


# ============================================================
# RULE-BASED FALLBACK
# ============================================================

RULE_TOPICS_EN = {

    "variable":
        "A variable stores a value so you can reuse it. "
        "Example: age = 18.",

    "loop":
        "A loop repeats code. A for loop iterates over values, "
        "while a while loop repeats while a condition is true.",

    "function":
        "A function is reusable code. "
        "Example: def greet(name): return 'Hello ' + name",

    "list":
        "A list stores multiple values in order. "
        "Example: fruits = ['apple', 'banana'].",

    "dictionary":
        "A dictionary stores key-value pairs. "
        "Example: student = {'name': 'Kabiru', 'age': 20}.",

    "sqlite":
        "SQLite is a lightweight file-based database. "
        "Python can use it with the sqlite3 module.",

    "fastapi":
        "FastAPI is a modern Python framework for building APIs. "
        "Routes can be created using decorators such as @app.get().",

    "git":
        "Git tracks changes in your source code. "
        "Common commands include git add, git commit and git push.",

    "class":
        "A class is a blueprint for creating objects in Python.",

    "error":
        "When Python shows an error, read the last line first. "
        "It normally tells you the exception type and problem.",

    "arduino":
        "Arduino is a microcontroller platform commonly used "
        "for electronics and embedded projects.",

    "esp32":
        "ESP32 is a microcontroller with built-in Wi-Fi and "
        "Bluetooth, commonly used for IoT.",

    "sensor":
        "A sensor detects a physical quantity such as temperature, "
        "light, distance or motion.",

    "circuit":
        "An electronic circuit connects components so electrical "
        "current can perform a useful function.",

    "robot":
        "A robot combines sensors, a controller and actuators "
        "to sense, decide and act.",

    "docker":
        "Docker packages applications and their dependencies "
        "inside containers."
}


RULE_TOPICS_HA = {

    "variable":
        "Variable wuri ne da ake ajiye bayani domin sake amfani da shi. "
        "Misali: age = 18.",

    "loop":
        "Loop yana maimaita code. For yana zagayawa cikin abubuwa, "
        "while kuma yana maimaitawa muddin sharadi gaskiya ne.",

    "function":
        "Function wani yanki ne na code da za ka iya sake amfani da shi. "
        "Ana rubuta shi da def.",

    "list":
        "List yana ajiye abubuwa da yawa a jere. "
        "Misali: fruits = ['apple', 'banana'].",

    "dictionary":
        "Dictionary yana ajiye key da value tare. "
        "Misali: student = {'name': 'Kabiru'}.",

    "sqlite":
        "SQLite database ne mai sauki wanda yake amfani da file. "
        "Python yana amfani da sqlite3 wajen aiki da shi.",

    "fastapi":
        "FastAPI framework ne na Python da ake amfani da shi "
        "wajen gina APIs.",

    "git":
        "Git yana bibiyar canje-canje a cikin code. "
        "Misalan umarni su ne git add, git commit da git push.",

    "class":
        "Class tsari ne da ake amfani da shi wajen kirkirar objects "
        "a Python.",

    "error":
        "Idan Python ya bada error, ka fara karanta layin karshe. "
        "Yawanci yana nuna irin kuskuren da ya faru.",

    "arduino":
        "Arduino microcontroller platform ne da ake amfani da shi "
        "wajen electronics da embedded projects.",

    "esp32":
        "ESP32 microcontroller ne mai Wi-Fi da Bluetooth, "
        "ana amfani da shi sosai wajen IoT.",

    "sensor":
        "Sensor yana gano abubuwa kamar zafi, haske, nisa ko motsi.",

    "circuit":
        "Circuit tsarin haɗin kayan lantarki ne wanda yake ba da "
        "damar current ya gudana.",

    "robot":
        "Robot yana hade sensors, controller da actuators domin "
        "ganewa, yanke shawara da aiki.",

    "docker":
        "Docker yana tattara application da dependencies dinsa "
        "cikin container."
}


def _rule_based_reply(
    message: str,
    language: str,
) -> str:

    topics = (
        RULE_TOPICS_HA
        if language == "ha"
        else RULE_TOPICS_EN
    )

    lowered = message.lower()

    for keyword, explanation in topics.items():

        if keyword in lowered:
            return explanation

    if language == "ha":

        return (
            "Na fahimci tambayarka, amma AI service ba ta samu "
            "ba a wannan lokacin. Ka sake gwadawa."
        )

    return (
        "I understand your question, but the AI service is "
        "temporarily unavailable. Please try again."
    )


# ============================================================
# PUBLIC API
# ============================================================

def get_tutor_reply(
    message: str,
    preferred_language: str | None = None,
    history: list[dict] | None = None,
) -> tuple[str, str]:
    """
    Return:
        (reply, language)

    Provider priority:
        1. Gemini
        2. Ollama
        3. Rule-based fallback
    """

    language = (
        preferred_language
        if preferred_language in ("en", "ha")
        else detect_language(message)
    )

    # --------------------------------------------------------
    # 1. GEMINI
    # --------------------------------------------------------

    if settings.GEMINI_API_KEY:

        reply = _ask_gemini(
            message,
            language,
            history=history,
        )

        if reply:
            return reply, language

    # --------------------------------------------------------
    # 2. OLLAMA
    # --------------------------------------------------------

    usable, model = _ollama_available()

    if usable and model:

        reply = _ask_ollama(
            message,
            language,
            model,
            history=history,
        )

        if reply:
            return reply, language

    # --------------------------------------------------------
    # 3. RULE BASED
    # --------------------------------------------------------

    return (
        _rule_based_reply(
            message,
            language,
        ),
        language,
    )


# ============================================================
# ERROR EXPLANATION
# ============================================================

def explain_error(
    error_text: str,
    language: str = "en",
) -> str:

    lowered = error_text.lower()

    mapping_en = [

        (
            "nameerror",
            "You used a variable or function name that "
            "doesn't exist yet. Check spelling and define "
            "it before using it."
        ),

        (
            "typeerror",
            "You used incompatible data types. "
            "Check the types of the values you are combining."
        ),

        (
            "indentationerror",
            "Python indentation is incorrect. "
            "Use consistent indentation, normally 4 spaces."
        ),

        (
            "syntaxerror",
            "There is a syntax problem in your Python code. "
            "Check missing colons, brackets or quotes."
        ),

        (
            "zerodivisionerror",
            "You tried to divide a number by zero."
        ),

        (
            "indexerror",
            "You tried to access a list position that does not exist."
        ),

        (
            "keyerror",
            "You tried to access a dictionary key that does not exist."
        ),

        (
            "modulenotfounderror",
            "Python cannot find the requested module or package."
        ),

        (
            "attributeerror",
            "The object does not have the method or attribute "
            "you tried to use."
        ),

        (
            "filenotfounderror",
            "Python could not find the file at the specified path."
        ),
    ]

    mapping_ha = [

        (
            "nameerror",
            "Ka yi amfani da sunan variable ko function wanda "
            "ba a bayyana ba. Duba spelling sannan ka bayyana shi."
        ),

        (
            "typeerror",
            "Ka yi amfani da nau'ukan bayanai da ba su dace ba. "
            "Duba irin data da kake hada."
        ),

        (
            "indentationerror",
            "Akwai matsalar indentation. Yi amfani da spaces 4 "
            "kamar yadda Python ya saba."
        ),

        (
            "syntaxerror",
            "Akwai matsalar syntax. Duba colon, brackets da quotes."
        ),

        (
            "zerodivisionerror",
            "Ka yi kokarin raba lamba da sifili."
        ),

        (
            "indexerror",
            "Ka yi kokarin samun index na list wanda babu shi."
        ),

        (
            "keyerror",
            "Ka nemi key a dictionary wanda babu shi."
        ),

        (
            "modulenotfounderror",
            "Python bai samu module ko package din da ake nema ba."
        ),

        (
            "attributeerror",
            "Object din ba shi da method ko attribute da ka kira."
        ),

        (
            "filenotfounderror",
            "Python bai samu file din da ka nuna ba."
        ),
    ]

    mapping = (
        mapping_ha
        if language == "ha"
        else mapping_en
    )

    for key, explanation in mapping:

        if key in lowered:
            return explanation

    if language == "ha":

        return (
            "Na ga error amma ban gane takamaiman irin sa ba. "
            "Duba layin karshe na error domin yawanci yana nuna "
            "ainihin matsalar."
        )

    return (
        "I detected an error but could not identify the exact "
        "type. Check the last line of the error message."
    )
