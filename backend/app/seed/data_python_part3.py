"""
Seed data for the Python course — Part 3 (Lessons 11-15).
"""

PYTHON_LESSONS_PART3 = [
    {
        "slug": "python-11-functions",
        "title": "11. Functions",
        "level": "beginner",
        "explanation": (
            "A function is a reusable block of code that performs a task. Define one with 'def name(parameters):' "
            "and call it with name(arguments). Functions can return a value with 'return'. Parameters can have "
            "default values, e.g. def greet(name='friend'). Functions make code organized, reusable, and easier "
            "to test."
        ),
        "examples": (
            "def add(a, b):\n"
            "    return a + b\n"
            "\n"
            "def greet(name=\"friend\"):\n"
            "    print(f\"Hello, {name}!\")\n"
            "\n"
            "result = add(3, 4)\n"
            "print(result)   # 7\n"
            "greet()         # Hello, friend!\n"
            "greet(\"Kabiru\") # Hello, Kabiru!\n"
        ),
        "practice": (
            "1. Write a function called square(n) that returns n squared\n"
            "2. Write a function called is_even(n) that returns True/False\n"
            "3. Write a function with a default parameter for a greeting message"
        ),
        "mini_project": (
            "Mini Project: Simple Math Toolkit\n"
            "Write functions add(a,b), subtract(a,b), multiply(a,b), divide(a,b). Divide should check for "
            "division by zero and return a friendly message instead of crashing. Call each function and "
            "print the results."
        ),
        "quiz": {
            "title": "Functions Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which keyword defines a function in Python?",
                    "option_a": "func",
                    "option_b": "def",
                    "option_c": "function",
                    "option_d": "define",
                    "correct_option": "b",
                    "explanation": "'def' is used to define a function in Python.",
                },
                {
                    "text": "What does 'return' do inside a function?",
                    "option_a": "Prints a value",
                    "option_b": "Sends a value back to the caller and ends the function",
                    "option_c": "Deletes the function",
                    "option_d": "Restarts the function",
                    "correct_option": "b",
                    "explanation": "'return' exits the function and passes a value back to wherever it was called.",
                },
                {
                    "text": "In def greet(name='friend'):, what happens if you call greet()?",
                    "option_a": "It raises an error",
                    "option_b": "name becomes 'friend' automatically",
                    "option_c": "name becomes None",
                    "option_d": "Nothing happens",
                    "correct_option": "b",
                    "explanation": "Default parameter values are used automatically when no argument is passed.",
                },
            ],
        },
    },
    {
        "slug": "python-12-scope",
        "title": "12. Variable Scope",
        "level": "beginner",
        "explanation": (
            "Scope determines where a variable can be accessed. Variables created inside a function are "
            "'local' and only exist within that function. Variables created outside any function are "
            "'global' and can be read anywhere, but you need the 'global' keyword to modify a global "
            "variable from inside a function."
        ),
        "examples": (
            "counter = 0   # global variable\n"
            "\n"
            "def increment():\n"
            "    global counter\n"
            "    counter += 1\n"
            "\n"
            "increment()\n"
            "print(counter)  # 1\n"
            "\n"
            "def local_example():\n"
            "    message = \"I only exist here\"\n"
            "    print(message)\n"
        ),
        "practice": (
            "1. Create a global variable total = 0\n"
            "2. Write a function that adds 10 to total using the global keyword\n"
            "3. Try printing a local variable from outside its function and observe the error"
        ),
        "mini_project": (
            "Mini Project: Bank Balance Tracker\n"
            "Create a global variable balance = 1000. Write deposit(amount) and withdraw(amount) functions "
            "that modify the global balance. Withdraw should prevent going negative."
        ),
        "quiz": {
            "title": "Variable Scope Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Where can a local variable be accessed?",
                    "option_a": "Anywhere in the program",
                    "option_b": "Only inside the function where it was created",
                    "option_c": "Only in other functions",
                    "option_d": "Only in the main file",
                    "correct_option": "b",
                    "explanation": "Local variables exist only within the function that created them.",
                },
                {
                    "text": "What keyword lets you modify a global variable inside a function?",
                    "option_a": "public",
                    "option_b": "global",
                    "option_c": "external",
                    "option_d": "outer",
                    "correct_option": "b",
                    "explanation": "'global' tells Python to use the global variable instead of creating a local one.",
                },
                {
                    "text": "Can you read a global variable inside a function without the 'global' keyword?",
                    "option_a": "No, never",
                    "option_b": "Yes, reading works fine without 'global'",
                    "option_c": "Only in Python 2",
                    "option_d": "Only if it's a number",
                    "correct_option": "b",
                    "explanation": "You only need 'global' to modify (reassign) a global variable, not just to read it.",
                },
            ],
        },
    },
    {
        "slug": "python-13-error-handling",
        "title": "13. Error Handling (try/except)",
        "level": "intermediate",
        "explanation": (
            "Errors (exceptions) can crash your program if not handled. Use try/except to catch errors "
            "gracefully. Put risky code in 'try:', and handle the error in 'except ExceptionType:'. You "
            "can use 'finally:' for code that always runs, and 'raise' to trigger your own exceptions."
        ),
        "examples": (
            "try:\n"
            "    number = int(input(\"Enter a number: \"))\n"
            "    result = 10 / number\n"
            "    print(result)\n"
            "except ZeroDivisionError:\n"
            "    print(\"You can't divide by zero!\")\n"
            "except ValueError:\n"
            "    print(\"That's not a valid number!\")\n"
            "finally:\n"
            "    print(\"Done trying.\")\n"
        ),
        "practice": (
            "1. Write code that divides two numbers and handles ZeroDivisionError\n"
            "2. Write code that converts user input to int and handles ValueError\n"
            "3. Add a finally block that prints 'Operation complete'"
        ),
        "mini_project": (
            "Mini Project: Safe Calculator\n"
            "Build a calculator that asks the user for two numbers and an operator (+, -, *, /). Use "
            "try/except to handle invalid numbers and division by zero without crashing."
        ),
        "quiz": {
            "title": "Error Handling Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which block contains code that might raise an error?",
                    "option_a": "except",
                    "option_b": "try",
                    "option_c": "finally",
                    "option_d": "catch",
                    "correct_option": "b",
                    "explanation": "Risky code goes inside the 'try' block.",
                },
                {
                    "text": "Which error occurs when dividing by zero?",
                    "option_a": "ValueError",
                    "option_b": "ZeroDivisionError",
                    "option_c": "TypeError",
                    "option_d": "NameError",
                    "correct_option": "b",
                    "explanation": "Dividing by zero raises a ZeroDivisionError in Python.",
                },
                {
                    "text": "What does the 'finally' block do?",
                    "option_a": "Only runs if there was an error",
                    "option_b": "Only runs if there was no error",
                    "option_c": "Always runs, error or not",
                    "option_d": "Never runs",
                    "correct_option": "c",
                    "explanation": "'finally' always executes, whether or not an exception occurred.",
                },
            ],
        },
    },
    {
        "slug": "python-14-file-io",
        "title": "14. File Input/Output",
        "level": "intermediate",
        "explanation": (
            "Python can read and write files using open(). The mode 'r' reads, 'w' writes (overwrites), "
            "'a' appends. Always use 'with open(...) as f:' so the file closes automatically. Use "
            "f.read(), f.readlines(), or loop over the file object to read lines; use f.write() to write."
        ),
        "examples": (
            "# Writing to a file\n"
            "with open(\"notes.txt\", \"w\") as f:\n"
            "    f.write(\"Kabiru is learning Python\\n\")\n"
            "\n"
            "# Reading from a file\n"
            "with open(\"notes.txt\", \"r\") as f:\n"
            "    content = f.read()\n"
            "    print(content)\n"
        ),
        "practice": (
            "1. Write 3 lines of text to a file called diary.txt\n"
            "2. Read the file back and print its contents\n"
            "3. Append one more line to the same file without erasing the previous content"
        ),
        "mini_project": (
            "Mini Project: Simple Notes App\n"
            "Write a script with a function save_note(text) that appends to notes.txt with a timestamp-like "
            "prefix, and a function show_notes() that reads and prints all saved notes."
        ),
        "quiz": {
            "title": "File I/O Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which mode opens a file for appending without deleting existing content?",
                    "option_a": "'r'",
                    "option_b": "'w'",
                    "option_c": "'a'",
                    "option_d": "'x'",
                    "correct_option": "c",
                    "explanation": "'a' (append) mode adds new content to the end of the file.",
                },
                {
                    "text": "Why use 'with open(...) as f:' instead of just open()?",
                    "option_a": "It's faster",
                    "option_b": "It automatically closes the file when done",
                    "option_c": "It's required by Python syntax",
                    "option_d": "It prevents reading the file",
                    "correct_option": "b",
                    "explanation": "The 'with' statement ensures the file is properly closed even if an error occurs.",
                },
                {
                    "text": "Which mode would ERASE existing file content before writing?",
                    "option_a": "'r'",
                    "option_b": "'a'",
                    "option_c": "'w'",
                    "option_d": "'read'",
                    "correct_option": "c",
                    "explanation": "'w' (write) mode overwrites the entire file content.",
                },
            ],
        },
    },
    {
        "slug": "python-15-modules",
        "title": "15. Modules and Imports",
        "level": "intermediate",
        "explanation": (
            "A module is a .py file containing code you can reuse in other files. Use 'import module_name' "
            "to bring in a whole module, or 'from module import thing' for specific parts. Python's "
            "standard library includes many built-in modules like math, random, datetime, and os."
        ),
        "examples": (
            "import math\n"
            "print(math.sqrt(16))    # 4.0\n"
            "\n"
            "from random import randint\n"
            "print(randint(1, 10))   # random number between 1 and 10\n"
            "\n"
            "import os\n"
            "print(os.getcwd())      # current working directory\n"
        ),
        "practice": (
            "1. Import the math module and print the value of math.pi\n"
            "2. Import random and generate 3 random numbers between 1 and 100\n"
            "3. Create your own module (mymodule.py) with a function, then import and use it in another file"
        ),
        "mini_project": (
            "Mini Project: Dice Rolling Game\n"
            "Use the random module to simulate rolling two dice. Print each die's value and their sum. "
            "Let the user roll again by asking yes/no with input()."
        ),
        "quiz": {
            "title": "Modules Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which keyword brings a module into your script?",
                    "option_a": "include",
                    "option_b": "import",
                    "option_c": "require",
                    "option_d": "use",
                    "correct_option": "b",
                    "explanation": "'import' is used to load a module in Python.",
                },
                {
                    "text": "Which module provides mathematical functions like sqrt()?",
                    "option_a": "os",
                    "option_b": "math",
                    "option_c": "random",
                    "option_d": "sys",
                    "correct_option": "b",
                    "explanation": "The math module provides functions like sqrt(), floor(), and constants like pi.",
                },
                {
                    "text": "What does 'from random import randint' do differently than 'import random'?",
                    "option_a": "It imports everything from random",
                    "option_b": "It imports only the randint function directly, usable without the random. prefix",
                    "option_c": "It's invalid syntax",
                    "option_d": "It deletes the random module",
                    "correct_option": "b",
                    "explanation": "'from module import name' imports a specific function/class directly into your namespace.",
                },
            ],
        },
    },
]
