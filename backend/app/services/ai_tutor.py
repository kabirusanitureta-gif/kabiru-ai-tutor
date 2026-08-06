"""
AI Tutor service.

Tries a local Ollama model first (if OLLAMA_ENABLED and Ollama is reachable).
The best installed model is auto-detected — no manual model name required.
If Ollama is not installed, not running, has no models, or times out, the
service falls back to a rule-based tutoring engine so the app ALWAYS works
offline with zero external dependencies and zero paid APIs.

Public functions (signatures never change, so callers like app/routers/chat.py
never need to change):
    get_tutor_reply(message, preferred_language=None) -> (reply: str, language: str)
    explain_error(error_text, language="en") -> str
    detect_language(text) -> "en" | "ha"
"""
import httpx

from app.core.config import settings

# ---------------------------------------------------------------------------
# Language detection (Hausa vs English)
# ---------------------------------------------------------------------------
# A compact list of very common Hausa words/markers used for lightweight
# language detection (no external NLP library needed -> works on Termux).
HAUSA_MARKERS = {
    "ina", "yaya", "menene", "don", "me", "yasa", "wannan", "wancan", "na",
    "ba", "ne", "ce", "ake", "yake", "zan", "zai", "ka", "ki", "mu", "ku",
    "su", "abin", "abu", "yaushe", "nawa", "sannu", "yaya kake", "godiya",
    "don allah", "abin da", "ina son", "koyi", "koya", "malam", "dalibi",
    "kuskure", "lambar", "shirin",
}


def detect_language(text: str) -> str:
    """Return 'ha' if text looks like Hausa, otherwise 'en'."""
    lowered = text.lower()
    words = set(lowered.replace(",", " ").replace(".", " ").split())
    hits = words.intersection(HAUSA_MARKERS)
    return "ha" if len(hits) >= 1 else "en"


# ---------------------------------------------------------------------------
# Ollama detection and automatic model selection
# ---------------------------------------------------------------------------
def _list_ollama_models() -> list[str]:
    """Returns the list of model names currently installed in the local
    Ollama instance (e.g. ['qwen2.5:7b', 'llama3.1:8b']), or [] if Ollama
    is unreachable or has no models installed."""
    if not settings.OLLAMA_ENABLED:
        return []
    try:
        resp = httpx.get(f"{settings.OLLAMA_BASE_URL}/api/tags", timeout=2.0)
        if resp.status_code != 200:
            return []
        data = resp.json()
        return [m.get("name", "") for m in data.get("models", []) if m.get("name")]
    except Exception:
        return []


def _pick_best_model(available_models: list[str]) -> str | None:
    """
    Chooses which installed Ollama model to use.

    - If OLLAMA_MODEL is explicitly set to something other than "auto" AND
      that exact model is installed, it wins (explicit override always wins).
    - Otherwise, scan settings.ollama_preferred_models_list in order
      (default priority: Qwen > DeepSeek > Llama > Gemma > Mistral) and
      return the first installed model whose name contains that family name.
    - If nothing in the priority list matches, fall back to whatever is
      installed (first available model), so any local model still works.
    - Returns None only if no models are installed at all.
    """
    if not available_models:
        return None

    explicit = settings.OLLAMA_MODEL.strip().lower()
    if explicit and explicit != "auto":
        for model in available_models:
            if model.lower() == explicit:
                return model
        # Explicit model requested but not installed — fall through to
        # auto-selection rather than failing outright.

    for family in settings.ollama_preferred_models_list:
        for model in available_models:
            if family in model.lower():
                return model

    # No preferred family matched — use whatever is installed rather than
    # refusing to use a perfectly good local model.
    return available_models[0]


def _ollama_available() -> tuple[bool, str | None]:
    """Returns (is_usable, chosen_model_name_or_None)."""
    models = _list_ollama_models()
    chosen = _pick_best_model(models)
    return (chosen is not None, chosen)


# ---------------------------------------------------------------------------
# System prompt: the AI's full area of expertise
# ---------------------------------------------------------------------------
_EXPERT_DOMAINS_EN = (
    "software engineering, Python, FastAPI, SQLite, PostgreSQL, Linux, Git, GitHub, "
    "HTML, CSS, JavaScript, TypeScript, React, Node.js, Docker, DevOps, networking, "
    "cybersecurity basics, algorithms and data structures, AI and machine learning "
    "fundamentals, electrical and electronics engineering, embedded systems, Arduino, "
    "ESP32, microcontrollers, PCB design basics, robotics, automation, IoT, and "
    "hardware engineering"
)
_EXPERT_DOMAINS_HA = (
    "injiniyan software, Python, FastAPI, SQLite, PostgreSQL, Linux, Git, GitHub, "
    "HTML, CSS, JavaScript, TypeScript, React, Node.js, Docker, DevOps, sadarwar "
    "network, tushen cyber security, algorithms da data structures, tushen AI da "
    "machine learning, injiniyan lantarki da electronics, embedded systems, Arduino, "
    "ESP32, microcontrollers, tushen PCB design, robotics, automation, IoT, da "
    "injiniyan hardware"
)


def _build_system_prompt(language: str) -> str:
    if language == "ha":
        return (
            "Kai ne Kabiru AI Tutor, malami ne mai hakuri, abokantaka, kuma gwani a "
            f"fannonin: {_EXPERT_DOMAINS_HA}. Ka bayyana abubuwa cikin sauki, ka yi "
            "amfani da gajerun misalai masu amfani, kuma ka karfafa dalibin gwiwa. "
            "Amsa cikin harshen Hausa kawai."
        )
    return (
        "You are Kabiru AI Tutor, a friendly, patient, and highly knowledgeable "
        f"expert across: {_EXPERT_DOMAINS_EN}. Explain concepts simply, use short "
        "practical examples, and be encouraging — the student may be a complete "
        "beginner or advancing toward expert level in any of these fields. "
        "Respond in English only."
    )


def _ask_ollama(prompt: str, language: str, model: str) -> str | None:
    system_prompt = _build_system_prompt(language)
    try:
        resp = httpx.post(
            f"{settings.OLLAMA_BASE_URL}/api/generate",
            json={
                "model": model,
                "prompt": f"{system_prompt}\n\nStudent: {prompt}\nTutor:",
                "stream": False,
            },
            timeout=60.0,
        )
        if resp.status_code == 200:
            data = resp.json()
            return data.get("response", "").strip()
    except Exception:
        return None
    return None


# ---------------------------------------------------------------------------
# Rule-based fallback tutor (works with ZERO external dependencies)
# ---------------------------------------------------------------------------
RULE_TOPICS_EN = {
    "variable": "A variable stores a value in memory so you can reuse it. "
                "Example: age = 18. In Python you don't declare a type; "
                "Python figures it out for you.",
    "loop": "A loop repeats code. 'for' loops iterate over a sequence, "
            "'while' loops repeat while a condition is True. "
            "Example: for i in range(5): print(i)",
    "function": "A function is a reusable block of code. Define it with "
                "'def name(parameters):' and call it with name(arguments).",
    "list": "A list stores multiple values in order: fruits = ['apple', 'banana']. "
            "You can add with .append(), access with fruits[0].",
    "dictionary": "A dictionary stores key-value pairs: student = {'name': 'Kabiru', "
                  "'age': 20}. Access with student['name'].",
    "sqlite": "SQLite is a lightweight file-based database. In Python use "
              "'import sqlite3', then sqlite3.connect('file.db') to start.",
    "fastapi": "FastAPI is a modern Python web framework. Define routes with "
               "@app.get('/path') and run with uvicorn.",
    "git": "Git tracks changes in your code. Common commands: git init, "
           "git add ., git commit -m 'message', git push.",
    "class": "A class is a blueprint for creating objects. Use 'class Name:' "
             "and define methods including __init__ for setup.",
    "error": "When you get an error, read the last line first — it usually "
             "names the exception type (e.g. TypeError, NameError) and the "
             "reason. Check the line number mentioned just above it.",
    "arduino": "Arduino is a beginner-friendly microcontroller platform. You "
               "write code (called a 'sketch') in a simplified C/C++ with "
               "setup() running once and loop() running repeatedly.",
    "esp32": "The ESP32 is a low-cost microcontroller with built-in Wi-Fi and "
             "Bluetooth, popular for IoT projects. It can be programmed with "
             "the Arduino IDE, MicroPython, or ESP-IDF.",
    "sensor": "A sensor converts a physical quantity (light, temperature, "
              "distance, motion) into an electrical signal your "
              "microcontroller can read, usually via analog or digital pins.",
    "circuit": "An electronic circuit is a closed loop of components (like "
               "resistors, LEDs, and power sources) that lets current flow "
               "to perform a function. Always check polarity and current "
               "limits before powering a circuit.",
    "robot": "A robot combines sensors (to perceive), a controller (to "
             "decide), and actuators like motors (to act). Robotics projects "
             "usually start with simple motor control before adding sensors.",
    "docker": "Docker packages an application with everything it needs into "
              "a 'container' that runs the same way anywhere. A Dockerfile "
              "defines how to build the image; 'docker build' and "
              "'docker run' create and start it.",
}

RULE_TOPICS_HA = {
    "variable": "Variable wuri ne da ake ajiye bayani domin sake amfani da shi. "
                "Misali: age = 18. A Python ba sai ka fada irin nau'in bayanin ba.",
    "loop": "Loop yana maimaita code. 'for' yana zagayawa cikin jerin abubuwa, "
            "'while' yana maimaitawa muddin sharadi gaskiya ne. "
            "Misali: for i in range(5): print(i)",
    "function": "Function wani yanki ne na code da za ka iya sake amfani da shi. "
                "Ana rubuta shi da 'def suna(parameters):' sannan a kira shi.",
    "list": "List yana ajiye abubuwa da yawa a jere: 'yan'itace = ['apple', 'banana']. "
            "Za ka iya kara abu da .append().",
    "dictionary": "Dictionary yana ajiye key da value tare: dalibi = {'suna': 'Kabiru', "
                  "'shekara': 20}. Ana samun dan bayani da dalibi['suna'].",
    "sqlite": "SQLite karamin database ne wanda ke amfani da file. A Python "
              "amfani da 'import sqlite3' sannan sqlite3.connect('file.db').",
    "fastapi": "FastAPI wani sabon tsarin gina web apps ne da Python. "
               "Ana rubuta hanya da @app.get('/path') sannan a gudanar da shi.",
    "git": "Git yana bibiyar canje-canje a cikin code dinka. Umarni na yau da kullum: "
           "git init, git add ., git commit -m 'sako', git push.",
    "class": "Class shine tsari na samar da objects. Ana amfani da 'class Suna:' "
             "sannan a rubuta methods hade da __init__ don farawa.",
    "error": "Idan ka samu kuskure (error), farko ka karanta layin karshe — yawanci "
             "shine ke gaya maka irin kuskuren (misali TypeError, NameError).",
    "arduino": "Arduino wani karamin kwamfuta ne (microcontroller) mai sauki ga "
               "masu farawa. Ana rubuta code (ana kiransa 'sketch') inda setup() "
               "ke gudana sau daya, sannan loop() ke maimaitawa.",
    "esp32": "ESP32 wani karamin microcontroller ne mai rahusa, dauke da Wi-Fi da "
             "Bluetooth a ciki, ana amfani da shi wajen ayyukan IoT.",
    "sensor": "Sensor yana canza wani abu na zahiri (haske, zafi, nisa, motsi) "
              "zuwa sigina na lantarki wanda microcontroller din ka zai iya karantawa.",
    "circuit": "Circuit din lantarki tsari ne na abubuwa (kamar resistor, LED, "
               "da tushen wutar lantarki) da ke bada damar wutar lantarki ta "
               "gudana domin yin aiki. Koyaushe ka duba polarity da iyakar "
               "current kafin ka bada wutar lantarki.",
    "robot": "Robot yana hade sensors (domin ganewa), controller (domin yanke "
             "shawara), da actuators kamar motoci (domin aiki). Ayyukan robotics "
             "yawanci suna farawa da sarrafa motor mai sauki kafin a kara sensors.",
    "docker": "Docker yana tattara app din ka tare da duk abin da yake bukata "
              "cikin 'container' wanda ke gudana daidai a ko'ina. Dockerfile "
              "yana bayyana yadda za a gina image din; 'docker build' da "
              "'docker run' suna kirkirawa da fara shi.",
}


def _rule_based_reply(message: str, language: str) -> str:
    topics = RULE_TOPICS_HA if language == "ha" else RULE_TOPICS_EN
    lowered = message.lower()
    for keyword, explanation in topics.items():
        if keyword in lowered:
            return explanation

    if language == "ha":
        return (
            "Na fahimci tambayarka. A yanzu ina aiki cikin yanayin koyarwa na "
            "asali (babu local AI model da ake amfani da shi a yanzu). Gwada "
            "tambayi game da: variable, loop, function, list, dictionary, class, "
            "sqlite, fastapi, git, error, arduino, esp32, sensor, circuit, "
            "robot, ko docker."
        )
    return (
        "I understand your question. I'm currently running in basic tutoring "
        "mode (no local AI model is active right now). Try asking about: "
        "variable, loop, function, list, dictionary, class, sqlite, fastapi, "
        "git, error, arduino, esp32, sensor, circuit, robot, or docker."
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def get_tutor_reply(message: str, preferred_language: str | None = None) -> tuple[str, str]:
    """
    Returns (reply, language_used).
    Auto-detects Hausa vs English unless preferred_language is explicitly set.
    Automatically uses the best installed local Ollama model if one is
    available; otherwise transparently falls back to the rule-based tutor.
    """
    language = preferred_language if preferred_language in ("en", "ha") else detect_language(message)

    usable, model = _ollama_available()
    if usable and model:
        reply = _ask_ollama(message, language, model)
        if reply:
            return reply, language

    return _rule_based_reply(message, language), language


def explain_error(error_text: str, language: str = "en") -> str:
    """Explain a Python error message in simple terms, bilingual."""
    lowered = error_text.lower()

    mapping_en = [
        ("nameerror", "You used a variable or function name that doesn't exist yet. Check spelling and make sure you defined it before using it."),
        ("typeerror", "You mixed incompatible types, e.g. adding text and a number. Convert types with str(), int(), or float()."),
        ("indentationerror", "Python cares about spacing. Make sure your code block is indented consistently (use 4 spaces)."),
        ("syntaxerror", "There's a typo or missing symbol (like a colon ':' or closing bracket) in your code."),
        ("zerodivisionerror", "You tried to divide a number by zero, which is not allowed."),
        ("indexerror", "You tried to access a list position that doesn't exist. Check the list length."),
        ("keyerror", "You tried to access a dictionary key that doesn't exist. Check the key name."),
        ("modulenotfounderror", "Python can't find that package. Install it with: pip install <package-name>."),
        ("attributeerror", "You called a method/property that doesn't exist on that object. Check spelling and object type."),
        ("filenotfounderror", "The file path you gave doesn't exist. Double check the path and filename."),
    ]
    mapping_ha = [
        ("nameerror", "Ka yi amfani da suna (variable/function) da ba a bayyana ba tukuna. Duba rubutu, sannan ka tabbata ka bayyana shi kafin amfani da shi."),
        ("typeerror", "Ka hade nau'ukan bayanai da ba su dace ba, misali rubutu da lamba. Yi amfani da str(), int(), ko float() don canzawa."),
        ("indentationerror", "Python yana kula da tazara (spacing). Tabbata code dinka yana da tazara daidai (spaces 4)."),
        ("syntaxerror", "Akwai kuskuren rubutu ko wani alama da ta bata (kamar ':' ko closing bracket) a cikin code dinka."),
        ("zerodivisionerror", "Ka yi kokarin raba lamba da sifili (0), wanda ba a yarda ba."),
        ("indexerror", "Ka yi kokarin samun matsayi a list wanda babu shi. Duba tsawon list dinka."),
        ("keyerror", "Ka yi kokarin samun key a dictionary wanda babu shi. Duba sunan key."),
        ("modulenotfounderror", "Python bai samu wannan package ba. Shigar da shi ta hanyar: pip install <sunan-package>."),
        ("attributeerror", "Ka kira method/property wanda babu shi akan wannan object. Duba rubutu da irin object din."),
        ("filenotfounderror", "Hanyar file da ka bayar babu ta. Duba sunan file da hanya sau biyu."),
    ]

    mapping = mapping_ha if language == "ha" else mapping_en
    for key, explanation in mapping:
        if key in lowered:
            return explanation

    if language == "ha":
        return "Na samu kuskure amma ban gane takamaiman irinsa ba. Karanta sakon kuskuren a hankali, layi na karshe yawanci yana bayyana matsalar."
    return "I detected an error but couldn't classify the exact type. Read the last line of the error carefully — it usually names the problem."
