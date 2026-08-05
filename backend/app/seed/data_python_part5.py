"""
Seed data for the Python course — Part 5 (Lessons 21-25).
"""

PYTHON_LESSONS_PART5 = [
    {
        "slug": "python-21-generators-iterators",
        "title": "21. Generators and Iterators",
        "level": "advanced",
        "explanation": (
            "An iterator is an object you can loop over one item at a time. A generator is a special "
            "function that produces items lazily using 'yield' instead of 'return'. Generators are "
            "memory-efficient because they don't store the whole sequence in memory at once — useful "
            "for large or infinite sequences."
        ),
        "examples": (
            "def count_up_to(n):\n"
            "    i = 1\n"
            "    while i <= n:\n"
            "        yield i\n"
            "        i += 1\n"
            "\n"
            "for number in count_up_to(5):\n"
            "    print(number)\n"
            "\n"
            "# Generator expression\n"
            "squares = (x ** 2 for x in range(5))\n"
            "print(list(squares))\n"
        ),
        "practice": (
            "1. Write a generator function that yields even numbers up to n\n"
            "2. Write a generator expression that yields cubes of numbers 1 to 10\n"
            "3. Use next() manually on a generator to get its first two values"
        ),
        "mini_project": (
            "Mini Project: Fibonacci Generator\n"
            "Write a generator function fibonacci(n) that yields the first n Fibonacci numbers. "
            "Print them using a for loop."
        ),
        "quiz": {
            "title": "Generators and Iterators Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which keyword makes a function a generator?",
                    "option_a": "return",
                    "option_b": "yield",
                    "option_c": "generate",
                    "option_d": "next",
                    "correct_option": "b",
                    "explanation": "'yield' produces a value and pauses the function, making it a generator.",
                },
                {
                    "text": "Why are generators memory-efficient?",
                    "option_a": "They compress data automatically",
                    "option_b": "They produce items one at a time instead of storing them all in memory",
                    "option_c": "They run on the GPU",
                    "option_d": "They use less CPU",
                    "correct_option": "b",
                    "explanation": "Generators compute values lazily, only when requested, avoiding full storage.",
                },
                {
                    "text": "Which brackets create a generator expression?",
                    "option_a": "[]",
                    "option_b": "{}",
                    "option_c": "()",
                    "option_d": "<>",
                    "correct_option": "c",
                    "explanation": "Parentheses create a generator expression, e.g. (x for x in range(5)).",
                },
            ],
        },
    },
    {
        "slug": "python-22-regex",
        "title": "22. Regular Expressions",
        "level": "advanced",
        "explanation": (
            "Regular expressions (regex) let you search, match, and manipulate text using patterns. "
            "Python's 're' module provides re.search(), re.match(), re.findall(), and re.sub(). "
            "Common patterns: \\d (digit), \\w (word character), + (one or more), * (zero or more)."
        ),
        "examples": (
            "import re\n"
            "\n"
            "text = \"My phone number is 08012345678\"\n"
            "match = re.search(r\"\\d{11}\", text)\n"
            "if match:\n"
            "    print(match.group())   # 08012345678\n"
            "\n"
            "emails = re.findall(r\"[\\w.]+@[\\w.]+\", \"Contact: kabiru@test.com or admin@site.ng\")\n"
            "print(emails)\n"
        ),
        "practice": (
            "1. Use re.search() to find a 4-digit year in a sentence\n"
            "2. Use re.findall() to extract all words starting with a capital letter\n"
            "3. Use re.sub() to replace all digits in a string with '#'"
        ),
        "mini_project": (
            "Mini Project: Simple Input Validator\n"
            "Write functions is_valid_email(text) and is_valid_phone(text) using regex patterns, "
            "and test them against a few sample strings."
        ),
        "quiz": {
            "title": "Regular Expressions Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which module provides regex support in Python?",
                    "option_a": "regex",
                    "option_b": "re",
                    "option_c": "pattern",
                    "option_d": "match",
                    "correct_option": "b",
                    "explanation": "Python's built-in regex module is called 're'.",
                },
                {
                    "text": "What does \\d represent in a regex pattern?",
                    "option_a": "Any letter",
                    "option_b": "Any digit",
                    "option_c": "A whitespace",
                    "option_d": "A dot character",
                    "correct_option": "b",
                    "explanation": "\\d matches any digit character (0-9).",
                },
                {
                    "text": "Which function returns ALL matches of a pattern in a string?",
                    "option_a": "re.search()",
                    "option_b": "re.match()",
                    "option_c": "re.findall()",
                    "option_d": "re.check()",
                    "correct_option": "c",
                    "explanation": "re.findall() returns a list of all non-overlapping matches in the string.",
                },
            ],
        },
    },
    {
        "slug": "python-23-datetime",
        "title": "23. Working with Dates and Time",
        "level": "intermediate",
        "explanation": (
            "The 'datetime' module handles dates and times. datetime.now() gives the current date and "
            "time. You can format dates with .strftime() and parse strings into dates with "
            "datetime.strptime(). The 'timedelta' class helps calculate differences between dates."
        ),
        "examples": (
            "from datetime import datetime, timedelta\n"
            "\n"
            "now = datetime.now()\n"
            "print(now.strftime(\"%Y-%m-%d %H:%M\"))\n"
            "\n"
            "tomorrow = now + timedelta(days=1)\n"
            "print(tomorrow.strftime(\"%Y-%m-%d\"))\n"
            "\n"
            "birthday = datetime.strptime(\"2000-05-15\", \"%Y-%m-%d\")\n"
            "print(birthday.year)\n"
        ),
        "practice": (
            "1. Print the current date and time formatted as DD/MM/YYYY\n"
            "2. Calculate and print the date 30 days from today\n"
            "3. Parse the string '2026-08-01' into a datetime object and print just the month"
        ),
        "mini_project": (
            "Mini Project: Age Calculator\n"
            "Ask the user for their birth year, month, and day. Calculate and print their current age "
            "in years using datetime."
        ),
        "quiz": {
            "title": "Dates and Time Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which function gives the current date and time?",
                    "option_a": "datetime.today_time()",
                    "option_b": "datetime.now()",
                    "option_c": "datetime.current()",
                    "option_d": "time.now()",
                    "correct_option": "b",
                    "explanation": "datetime.now() returns the current local date and time.",
                },
                {
                    "text": "Which method formats a datetime object into a string?",
                    "option_a": ".format()",
                    "option_b": ".strftime()",
                    "option_c": ".to_string()",
                    "option_d": ".display()",
                    "correct_option": "b",
                    "explanation": "strftime() converts a datetime object to a formatted string.",
                },
                {
                    "text": "Which class is used to represent a duration/difference between dates?",
                    "option_a": "duration",
                    "option_b": "timedelta",
                    "option_c": "timespan",
                    "option_d": "dateDiff",
                    "correct_option": "b",
                    "explanation": "timedelta represents a difference between two dates or times.",
                },
            ],
        },
    },
    {
        "slug": "python-24-json",
        "title": "24. Working with JSON",
        "level": "intermediate",
        "explanation": (
            "JSON (JavaScript Object Notation) is a common text format for exchanging data, especially "
            "with web APIs. Python's 'json' module converts between JSON text and Python objects: "
            "json.dumps() turns a Python object into a JSON string, and json.loads() parses JSON text "
            "into a Python object (usually a dict or list)."
        ),
        "examples": (
            "import json\n"
            "\n"
            "student = {\"name\": \"Kabiru\", \"age\": 20, \"skills\": [\"Python\", \"SQLite\"]}\n"
            "\n"
            "json_text = json.dumps(student, indent=2)\n"
            "print(json_text)\n"
            "\n"
            "parsed = json.loads(json_text)\n"
            "print(parsed[\"name\"])\n"
        ),
        "practice": (
            "1. Convert a Python dictionary to a JSON string with json.dumps()\n"
            "2. Convert a JSON string back into a Python dictionary with json.loads()\n"
            "3. Save a dictionary to a .json file using json.dump() and read it back with json.load()"
        ),
        "mini_project": (
            "Mini Project: Student Records JSON Store\n"
            "Create a list of student dictionaries, save it to students.json using json.dump(), then "
            "write a separate function that loads the file and prints all student names."
        ),
        "quiz": {
            "title": "JSON Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which function converts a Python dict into a JSON string?",
                    "option_a": "json.loads()",
                    "option_b": "json.dumps()",
                    "option_c": "json.parse()",
                    "option_d": "json.encode()",
                    "correct_option": "b",
                    "explanation": "json.dumps() serializes a Python object into a JSON-formatted string.",
                },
                {
                    "text": "Which function converts a JSON string into a Python object?",
                    "option_a": "json.loads()",
                    "option_b": "json.dumps()",
                    "option_c": "json.write()",
                    "option_d": "json.decode()",
                    "correct_option": "a",
                    "explanation": "json.loads() parses a JSON string into a Python dict/list.",
                },
                {
                    "text": "What Python type does a JSON object usually become?",
                    "option_a": "list",
                    "option_b": "dict",
                    "option_c": "tuple",
                    "option_d": "set",
                    "correct_option": "b",
                    "explanation": "A JSON object (key-value pairs) maps naturally to a Python dictionary.",
                },
            ],
        },
    },
    {
        "slug": "python-25-apis-requests",
        "title": "25. Working with APIs (requests)",
        "level": "advanced",
        "explanation": (
            "APIs let programs talk to each other over the internet. The 'requests' library (install "
            "with pip install requests) makes HTTP calls easy: requests.get(url) fetches data, and "
            ".json() parses a JSON response directly into a Python object. Always check response.status_code "
            "to confirm the request succeeded (200 means OK)."
        ),
        "examples": (
            "import requests\n"
            "\n"
            "response = requests.get(\"https://api.github.com\")\n"
            "print(response.status_code)   # 200 if successful\n"
            "\n"
            "if response.status_code == 200:\n"
            "    data = response.json()\n"
            "    print(data)\n"
        ),
        "practice": (
            "1. Install requests with: pip install requests\n"
            "2. Make a GET request to a public API and print the status code\n"
            "3. Parse the JSON response and print one specific field from it"
        ),
        "mini_project": (
            "Mini Project: Weather-Style API Client\n"
            "Write a function fetch_data(url) that makes a GET request, checks the status code, and "
            "returns the parsed JSON data or an error message if the request fails."
        ),
        "quiz": {
            "title": "APIs and Requests Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which library is commonly used to make HTTP requests in Python?",
                    "option_a": "http",
                    "option_b": "requests",
                    "option_c": "web",
                    "option_d": "api",
                    "correct_option": "b",
                    "explanation": "'requests' is the most widely used Python library for HTTP calls.",
                },
                {
                    "text": "What status code typically means a request succeeded?",
                    "option_a": "404",
                    "option_b": "500",
                    "option_c": "200",
                    "option_d": "301",
                    "correct_option": "c",
                    "explanation": "HTTP status code 200 means 'OK' — the request was successful.",
                },
                {
                    "text": "Which method parses a JSON API response into a Python object?",
                    "option_a": "response.text()",
                    "option_b": "response.json()",
                    "option_c": "response.parse()",
                    "option_d": "response.dict()",
                    "correct_option": "b",
                    "explanation": "response.json() converts the JSON response body into a Python dict/list.",
                },
            ],
        },
    },
]
