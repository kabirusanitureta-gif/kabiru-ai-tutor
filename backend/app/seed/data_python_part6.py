"""
Seed data for the Python course — Part 6 (Lessons 26-30, final batch).
"""

PYTHON_LESSONS_PART6 = [
    {
        "slug": "python-26-venv-pip",
        "title": "26. Virtual Environments and pip",
        "level": "intermediate",
        "explanation": (
            "A virtual environment is an isolated Python installation for a single project, so its "
            "packages don't conflict with other projects. Create one with 'python -m venv venv', "
            "activate it (source venv/bin/activate on Linux/Mac, venv\\Scripts\\activate on Windows), "
            "then install packages with 'pip install package_name'. Use 'pip freeze > requirements.txt' "
            "to save your project's dependencies."
        ),
        "examples": (
            "# Create a virtual environment\n"
            "python -m venv venv\n"
            "\n"
            "# Activate it (Linux/Mac/Termux)\n"
            "source venv/bin/activate\n"
            "\n"
            "# Install a package\n"
            "pip install requests\n"
            "\n"
            "# Save dependencies\n"
            "pip freeze > requirements.txt\n"
            "\n"
            "# Install from requirements.txt later\n"
            "pip install -r requirements.txt\n"
        ),
        "practice": (
            "1. Create a virtual environment called venv in a new folder\n"
            "2. Activate it and confirm with 'which python' (Linux) that it points inside venv\n"
            "3. Install any package, then run pip freeze to see it listed"
        ),
        "mini_project": (
            "Mini Project: Project Starter Kit\n"
            "Set up a new folder with a virtual environment, install requests and reportlab, then "
            "generate a requirements.txt file documenting both dependencies."
        ),
        "quiz": {
            "title": "Virtual Environments Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Why use a virtual environment?",
                    "option_a": "To make Python run faster",
                    "option_b": "To isolate a project's packages from other projects",
                    "option_c": "It's required to run any Python file",
                    "option_d": "To connect to the internet",
                    "correct_option": "b",
                    "explanation": "Virtual environments prevent dependency conflicts between different projects.",
                },
                {
                    "text": "Which command creates a virtual environment?",
                    "option_a": "python -m venv venv",
                    "option_b": "pip create venv",
                    "option_c": "python venv --new",
                    "option_d": "venv init",
                    "correct_option": "a",
                    "explanation": "python -m venv <name> creates a new virtual environment folder.",
                },
                {
                    "text": "What does 'pip freeze > requirements.txt' do?",
                    "option_a": "Deletes all installed packages",
                    "option_b": "Saves the list of installed packages and versions to a file",
                    "option_c": "Freezes the Python interpreter",
                    "option_d": "Installs packages from the internet",
                    "correct_option": "b",
                    "explanation": "pip freeze outputs installed packages; redirecting it saves them to requirements.txt.",
                },
            ],
        },
    },
    {
        "slug": "python-27-unit-testing",
        "title": "27. Unit Testing with unittest",
        "level": "advanced",
        "explanation": (
            "Unit tests check that individual pieces of your code work correctly. Python's built-in "
            "'unittest' module lets you write test classes with methods starting with 'test_'. Use "
            "assertions like self.assertEqual(), self.assertTrue(), self.assertRaises() to verify "
            "expected behavior. Run tests with: python -m unittest test_file.py"
        ),
        "examples": (
            "# math_utils.py\n"
            "def add(a, b):\n"
            "    return a + b\n"
            "\n"
            "# test_math_utils.py\n"
            "import unittest\n"
            "from math_utils import add\n"
            "\n"
            "class TestMathUtils(unittest.TestCase):\n"
            "    def test_add_positive_numbers(self):\n"
            "        self.assertEqual(add(2, 3), 5)\n"
            "\n"
            "    def test_add_negative_numbers(self):\n"
            "        self.assertEqual(add(-1, -1), -2)\n"
            "\n"
            "if __name__ == \"__main__\":\n"
            "    unittest.main()\n"
        ),
        "practice": (
            "1. Write a function is_palindrome(text) that checks if a string reads the same backward\n"
            "2. Write at least 3 unittest test cases for it (a palindrome, a non-palindrome, an empty string)\n"
            "3. Run the tests with python -m unittest and confirm they pass"
        ),
        "mini_project": (
            "Mini Project: Tested Calculator Module\n"
            "Build a calculator.py with add, subtract, multiply, divide functions (divide should raise "
            "ValueError on zero division). Write a full unittest test suite covering normal cases and "
            "the zero-division error case using self.assertRaises()."
        ),
        "quiz": {
            "title": "Unit Testing Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What prefix must test methods have in a unittest.TestCase class?",
                    "option_a": "check_",
                    "option_b": "test_",
                    "option_c": "verify_",
                    "option_d": "assert_",
                    "correct_option": "b",
                    "explanation": "unittest automatically discovers and runs methods starting with 'test_'.",
                },
                {
                    "text": "Which assertion checks that two values are equal?",
                    "option_a": "self.assertSame()",
                    "option_b": "self.assertEqual()",
                    "option_c": "self.equals()",
                    "option_d": "self.checkEqual()",
                    "correct_option": "b",
                    "explanation": "self.assertEqual(a, b) verifies that a and b are equal.",
                },
                {
                    "text": "Which assertion checks that a function raises a specific exception?",
                    "option_a": "self.assertError()",
                    "option_b": "self.assertRaises()",
                    "option_c": "self.expectError()",
                    "option_d": "self.catchException()",
                    "correct_option": "b",
                    "explanation": "self.assertRaises(ExceptionType) verifies that code raises the expected exception.",
                },
            ],
        },
    },
    {
        "slug": "python-28-context-managers",
        "title": "28. Context Managers",
        "level": "advanced",
        "explanation": (
            "Context managers handle setup and cleanup automatically using the 'with' statement, like "
            "closing a file or releasing a resource even if an error occurs. You've already used one: "
            "'with open(...) as f:'. You can create your own using a class with __enter__ and __exit__ "
            "methods, or more simply with the @contextmanager decorator from the contextlib module."
        ),
        "examples": (
            "from contextlib import contextmanager\n"
            "import time\n"
            "\n"
            "@contextmanager\n"
            "def timer():\n"
            "    start = time.time()\n"
            "    yield\n"
            "    end = time.time()\n"
            "    print(f\"Took {end - start:.4f} seconds\")\n"
            "\n"
            "with timer():\n"
            "    total = sum(range(1000000))\n"
        ),
        "practice": (
            "1. Write a custom context manager class with __enter__ and __exit__ that prints 'Opening' "
            "and 'Closing'\n"
            "2. Rewrite the same logic using @contextmanager and a generator function\n"
            "3. Use your context manager in a 'with' block"
        ),
        "mini_project": (
            "Mini Project: Database Connection Simulator\n"
            "Write a context manager (class-based) called FakeDBConnection that prints 'Connected' on "
            "__enter__ and 'Disconnected' on __exit__, even if an error happens inside the 'with' block. "
            "Test it by intentionally causing an error inside the block."
        ),
        "quiz": {
            "title": "Context Managers Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which statement uses a context manager?",
                    "option_a": "try",
                    "option_b": "with",
                    "option_c": "def",
                    "option_d": "class",
                    "correct_option": "b",
                    "explanation": "The 'with' statement is used to invoke a context manager's setup/cleanup.",
                },
                {
                    "text": "Which two methods does a class-based context manager need?",
                    "option_a": "__start__ and __stop__",
                    "option_b": "__enter__ and __exit__",
                    "option_c": "__open__ and __close__",
                    "option_d": "__init__ and __del__",
                    "correct_option": "b",
                    "explanation": "__enter__ runs at the start of the 'with' block, __exit__ runs at the end (even on error).",
                },
                {
                    "text": "Which decorator simplifies writing a context manager as a generator function?",
                    "option_a": "@staticmethod",
                    "option_b": "@contextmanager",
                    "option_c": "@property",
                    "option_d": "@classmethod",
                    "correct_option": "b",
                    "explanation": "@contextmanager (from contextlib) turns a generator function into a context manager.",
                },
            ],
        },
    },
    {
        "slug": "python-29-concurrency-basics",
        "title": "29. Concurrency Basics (Threading & Multiprocessing)",
        "level": "advanced",
        "explanation": (
            "Concurrency lets a program do multiple things at once. The 'threading' module runs tasks "
            "concurrently within one process — good for I/O-bound tasks like network requests. The "
            "'multiprocessing' module runs tasks in separate processes — good for CPU-bound tasks, "
            "since it bypasses Python's Global Interpreter Lock (GIL)."
        ),
        "examples": (
            "import threading\n"
            "import time\n"
            "\n"
            "def worker(name):\n"
            "    print(f\"{name} starting\")\n"
            "    time.sleep(1)\n"
            "    print(f\"{name} done\")\n"
            "\n"
            "t1 = threading.Thread(target=worker, args=(\"Thread-1\",))\n"
            "t2 = threading.Thread(target=worker, args=(\"Thread-2\",))\n"
            "t1.start()\n"
            "t2.start()\n"
            "t1.join()\n"
            "t2.join()\n"
        ),
        "practice": (
            "1. Write a function that sleeps for 2 seconds and prints a message\n"
            "2. Run it 3 times sequentially and time the total; then run it using 3 threads and time "
            "again\n"
            "3. Compare the two timings and note the difference"
        ),
        "mini_project": (
            "Mini Project: Parallel Downloader Simulator\n"
            "Simulate 'downloading' 5 files by sleeping for a random short time in each. Use threading "
            "to run all 5 'downloads' concurrently, printing when each starts and finishes."
        ),
        "quiz": {
            "title": "Concurrency Basics Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which module is best suited for I/O-bound concurrent tasks?",
                    "option_a": "threading",
                    "option_b": "math",
                    "option_c": "statistics",
                    "option_d": "itertools",
                    "correct_option": "a",
                    "explanation": "threading works well for I/O-bound tasks like network calls or file access.",
                },
                {
                    "text": "Why might multiprocessing be preferred over threading for CPU-heavy work?",
                    "option_a": "It uses less memory always",
                    "option_b": "It bypasses the GIL by using separate processes",
                    "option_c": "It's simpler to write",
                    "option_d": "Threading doesn't work on Linux",
                    "correct_option": "b",
                    "explanation": "multiprocessing uses separate processes, avoiding Python's GIL limitation for CPU-bound work.",
                },
                {
                    "text": "What does t.join() do for a thread t?",
                    "option_a": "Starts the thread",
                    "option_b": "Waits for the thread to finish before continuing",
                    "option_c": "Kills the thread immediately",
                    "option_d": "Merges two threads into one",
                    "correct_option": "b",
                    "explanation": "join() blocks the calling code until the thread completes.",
                },
            ],
        },
    },
    {
        "slug": "python-30-final-cli-project",
        "title": "30. Final Project: Building a CLI App",
        "level": "advanced",
        "explanation": (
            "This capstone lesson combines everything from the Python course — functions, classes, "
            "file I/O, error handling, and JSON — into one command-line application. You'll build a "
            "'Task Manager' CLI that lets a user add, list, complete, and delete tasks, saving them "
            "persistently to a JSON file so data survives between runs."
        ),
        "examples": (
            "import json, os\n"
            "\n"
            "TASKS_FILE = \"tasks.json\"\n"
            "\n"
            "def load_tasks():\n"
            "    if not os.path.exists(TASKS_FILE):\n"
            "        return []\n"
            "    with open(TASKS_FILE, \"r\") as f:\n"
            "        return json.load(f)\n"
            "\n"
            "def save_tasks(tasks):\n"
            "    with open(TASKS_FILE, \"w\") as f:\n"
            "        json.dump(tasks, f, indent=2)\n"
            "\n"
            "def add_task(title):\n"
            "    tasks = load_tasks()\n"
            "    tasks.append({\"title\": title, \"done\": False})\n"
            "    save_tasks(tasks)\n"
            "    print(f\"Added: {title}\")\n"
        ),
        "practice": (
            "1. Implement load_tasks() and save_tasks() as shown\n"
            "2. Implement list_tasks() that prints all tasks with their done status\n"
            "3. Implement complete_task(index) and delete_task(index) with proper error handling for "
            "invalid indexes"
        ),
        "mini_project": (
            "Capstone Project: Complete Task Manager CLI\n"
            "Build a full command-line menu (using a while loop and input()) offering: Add task, List "
            "tasks, Complete task, Delete task, Exit. All data must persist in tasks.json between runs. "
            "Use try/except so invalid menu choices or indexes never crash the program. This project "
            "demonstrates mastery of the entire Python course."
        ),
        "quiz": {
            "title": "Final CLI Project Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Why save tasks to a JSON file instead of keeping them only in a list variable?",
                    "option_a": "JSON files run faster",
                    "option_b": "Data persists between separate runs of the program",
                    "option_c": "Lists can't hold dictionaries",
                    "option_d": "It's required by Python syntax",
                    "correct_option": "b",
                    "explanation": "Saving to a file means the data survives even after the program exits and restarts.",
                },
                {
                    "text": "What should happen if the tasks.json file doesn't exist yet when loading?",
                    "option_a": "The program should crash",
                    "option_b": "Return an empty list so the program can still run",
                    "option_c": "Delete the program",
                    "option_d": "Wait forever",
                    "correct_option": "b",
                    "explanation": "Handling the missing-file case gracefully (returning []) keeps the app robust.",
                },
                {
                    "text": "Why wrap task index operations in try/except in the CLI menu?",
                    "option_a": "To make the code longer",
                    "option_b": "To prevent crashes from invalid user input like out-of-range indexes",
                    "option_c": "It's not necessary",
                    "option_d": "To slow down the program intentionally",
                    "correct_option": "b",
                    "explanation": "try/except protects against crashes when users enter invalid or out-of-range indexes.",
                },
            ],
        },
    },
]
