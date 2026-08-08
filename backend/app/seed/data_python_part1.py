"""
Seed data for the Python course — Part 1 (Lessons 1-10).
Each lesson dict matches the Lesson model fields plus an embedded quiz.
Further lessons (11-30) are added in data_python_part2.py and part3.py.
"""

PYTHON_LESSONS_PART1 = [
    {
        "slug": "python-01-introduction",
        "title": "1. Introduction to Python",
        "level": "beginner",
        "explanation": (
            "Python is a high-level, easy-to-read programming language used for web development, "
            "automation, data science, and AI. It was created by Guido van Rossum and released in 1991. "
            "Python code is executed line by line by an interpreter, so you don't need to compile it "
            "before running. You write a file ending in .py and run it with the command: python file.py"
        ),
        "examples": (
            "# Your first Python program\n"
            "print(\"Hello, Kabiru!\")\n"
            "print(\"Welcome to Python programming\")\n"
        ),
        "practice": (
            "1. Open a new file called hello.py\n"
            "2. Print your own name using print()\n"
            "3. Print a second line saying what you want to learn today\n"
            "4. Run the file with: python hello.py"
        ),
        "mini_project": (
            "Mini Project: Personal Greeting Script\n"
            "Write a script that prints your name, your city, and one goal you have for learning to code. "
            "Use three separate print() statements."
        ),
        "quiz": {
            "title": "Introduction to Python Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which function is used to display output in Python?",
                    "option_a": "print()",
                    "option_b": "display()",
                    "option_c": "echo()",
                    "option_d": "show()",
                    "correct_option": "a",
                    "explanation": "print() is the built-in function used to output text to the console.",
                },
                {
                    "text": "What file extension do Python files use?",
                    "option_a": ".py",
                    "option_b": ".python",
                    "option_c": ".pt",
                    "option_d": ".pyt",
                    "correct_option": "a",
                    "explanation": "Python source files use the .py extension.",
                },
                {
                    "text": "Is Python a compiled or interpreted language?",
                    "option_a": "Compiled only",
                    "option_b": "Interpreted",
                    "option_c": "Neither",
                    "option_d": "Assembly-based",
                    "correct_option": "b",
                    "explanation": "Python is interpreted — code runs line by line by the Python interpreter.",
                },
            ],
        },
    },
    {
        "slug": "python-02-variables",
        "title": "2. Variables and Assignment",
        "level": "beginner",
        "explanation": (
            "A variable is a name that refers to a value stored in memory. In Python, you create a "
            "variable simply by assigning a value to a name using the = sign. Python is dynamically "
            "typed, meaning you don't need to declare the variable's type — Python figures it out "
            "automatically based on the value you assign."
        ),
        "examples": (
            "name = \"Kabiru\"\n"
            "age = 20\n"
            "height = 1.75\n"
            "is_student = True\n"
            "print(name, age, height, is_student)\n"
        ),
        "practice": (
            "1. Create a variable called city and assign your city's name\n"
            "2. Create a variable called year and assign the current year\n"
            "3. Print both variables in one print() statement separated by a comma"
        ),
        "mini_project": (
            "Mini Project: Profile Card\n"
            "Create variables for name, age, course, and favorite_language. Print them formatted as:\n"
            "'Name: X | Age: Y | Course: Z | Favorite Language: W'"
        ),
        "quiz": {
            "title": "Variables Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How do you assign the value 5 to a variable called x?",
                    "option_a": "x == 5",
                    "option_b": "x = 5",
                    "option_c": "5 = x",
                    "option_d": "let x = 5",
                    "correct_option": "b",
                    "explanation": "A single = is used for assignment in Python.",
                },
                {
                    "text": "What type of typing does Python use?",
                    "option_a": "Static typing only",
                    "option_b": "Dynamic typing",
                    "option_c": "No typing at all",
                    "option_d": "Manual typing",
                    "correct_option": "b",
                    "explanation": "Python uses dynamic typing — types are determined automatically at runtime.",
                },
                {
                    "text": "Which of these is a valid Python variable name?",
                    "option_a": "2name",
                    "option_b": "my-name",
                    "option_c": "my_name",
                    "option_d": "my name",
                    "correct_option": "c",
                    "explanation": "Variable names can contain letters, numbers, and underscores, but can't start with a number or contain spaces/hyphens.",
                },
            ],
        },
    },
    {
        "slug": "python-03-data-types",
        "title": "3. Data Types",
        "level": "beginner",
        "explanation": (
            "Python has several built-in data types: int (whole numbers), float (decimal numbers), "
            "str (text), bool (True/False), list, tuple, dict, and set. You can check a variable's "
            "type using the type() function. Understanding data types helps you know what operations "
            "are valid on a value."
        ),
        "examples": (
            "age = 20                # int\n"
            "price = 19.99           # float\n"
            "name = \"Kabiru\"         # str\n"
            "is_active = True        # bool\n"
            "print(type(age))\n"
            "print(type(price))\n"
        ),
        "practice": (
            "1. Create one variable of each type: int, float, str, bool\n"
            "2. Use type() to print the type of each variable\n"
            "3. Try converting a string number '10' to an int using int('10')"
        ),
        "mini_project": (
            "Mini Project: Type Checker Tool\n"
            "Write a script with 5 different variables of mixed types. Loop through them (using a list) "
            "and print each value along with its type."
        ),
        "quiz": {
            "title": "Data Types Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which function tells you the data type of a variable?",
                    "option_a": "typeof()",
                    "option_b": "type()",
                    "option_c": "datatype()",
                    "option_d": "kind()",
                    "correct_option": "b",
                    "explanation": "type() returns the type of any Python object.",
                },
                {
                    "text": "What data type is the value True?",
                    "option_a": "int",
                    "option_b": "str",
                    "option_c": "bool",
                    "option_d": "float",
                    "correct_option": "c",
                    "explanation": "True and False are boolean (bool) values.",
                },
                {
                    "text": "What does int('10') do?",
                    "option_a": "Creates a syntax error",
                    "option_b": "Converts the string '10' to the integer 10",
                    "option_c": "Converts 10 to a string",
                    "option_d": "Deletes the variable",
                    "correct_option": "b",
                    "explanation": "int() converts a compatible string or float into an integer.",
                },
            ],
        },
    },
    {
        "slug": "python-04-operators",
        "title": "4. Operators",
        "level": "beginner",
        "explanation": (
            "Operators perform actions on values. Arithmetic operators (+, -, *, /, //, %, **) do math. "
            "Comparison operators (==, !=, >, <, >=, <=) compare values and return True/False. Logical "
            "operators (and, or, not) combine boolean expressions."
        ),
        "examples": (
            "a = 10\n"
            "b = 3\n"
            "print(a + b)   # 13\n"
            "print(a // b)  # 3  (floor division)\n"
            "print(a % b)   # 1  (remainder)\n"
            "print(a > b)   # True\n"
            "print(a > 5 and b < 5)  # True\n"
        ),
        "practice": (
            "1. Create two variables x and y with numbers\n"
            "2. Print the result of +, -, *, /, //, %, and ** on them\n"
            "3. Print a comparison using > and one using =="
        ),
        "mini_project": (
            "Mini Project: Simple Calculator\n"
            "Ask the user for two numbers with input(), convert them to float, then print the results "
            "of all arithmetic operations between them."
        ),
        "quiz": {
            "title": "Operators Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does the % operator return?",
                    "option_a": "The percentage of a number",
                    "option_b": "The remainder of division",
                    "option_c": "The power of a number",
                    "option_d": "A random number",
                    "correct_option": "b",
                    "explanation": "% is the modulo operator, returning the remainder after division.",
                },
                {
                    "text": "What does ** do in Python?",
                    "option_a": "Multiplication",
                    "option_b": "Exponentiation (power)",
                    "option_c": "Integer division",
                    "option_d": "Comment marker",
                    "correct_option": "b",
                    "explanation": "** raises a number to a power, e.g. 2 ** 3 = 8.",
                },
                {
                    "text": "Which operator checks if two values are equal?",
                    "option_a": "=",
                    "option_b": "==",
                    "option_c": "===",
                    "option_d": "equals()",
                    "correct_option": "b",
                    "explanation": "== compares two values for equality and returns a boolean.",
                },
            ],
        },
    },
    {
        "slug": "python-05-strings",
        "title": "5. Strings",
        "level": "beginner",
        "explanation": (
            "Strings are sequences of characters used for text. You can create them with single or "
            "double quotes. Strings support slicing, concatenation (+), repetition (*), and many "
            "built-in methods like .upper(), .lower(), .strip(), .split(), and .replace(). f-strings "
            "let you embed variables directly inside text."
        ),
        "examples": (
            "name = \"Kabiru\"\n"
            "greeting = f\"Hello, {name}! You have {5} new messages.\"\n"
            "print(greeting)\n"
            "print(name.upper())\n"
            "print(name[0:3])   # slicing -> 'Kab'\n"
        ),
        "practice": (
            "1. Create a string with your full name\n"
            "2. Print it in uppercase and lowercase\n"
            "3. Use an f-string to print 'My name is X and it has Y letters' using len()"
        ),
        "mini_project": (
            "Mini Project: Username Generator\n"
            "Take a first name and last name, and generate a username by combining the first 3 letters "
            "of the first name (lowercase) with the last name and a random-looking number, e.g. kab_sani99."
        ),
        "quiz": {
            "title": "Strings Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does f\"{name}\" do in an f-string?",
                    "option_a": "Formats the string in French",
                    "option_b": "Inserts the value of the variable name into the string",
                    "option_c": "Deletes the variable",
                    "option_d": "Converts name to a float",
                    "correct_option": "b",
                    "explanation": "f-strings embed variable values directly into text using curly braces.",
                },
                {
                    "text": "What does 'hello'.upper() return?",
                    "option_a": "'hello'",
                    "option_b": "'HELLO'",
                    "option_c": "'Hello'",
                    "option_d": "An error",
                    "correct_option": "b",
                    "explanation": ".upper() converts all characters in a string to uppercase.",
                },
                {
                    "text": "What does len('Kabiru') return?",
                    "option_a": "5",
                    "option_b": "6",
                    "option_c": "7",
                    "option_d": "'Kabiru'",
                    "correct_option": "b",
                    "explanation": "'Kabiru' has 6 characters, so len() returns 6.",
                },
            ],
        },
    },
]
