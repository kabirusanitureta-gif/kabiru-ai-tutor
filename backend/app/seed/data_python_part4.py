"""
Seed data for the Python course — Part 4 (Lessons 16-20).
"""

PYTHON_LESSONS_PART4 = [
    {
        "slug": "python-16-classes-objects",
        "title": "16. Classes and Objects",
        "level": "intermediate",
        "explanation": (
            "Object-Oriented Programming (OOP) organizes code around objects. A class is a blueprint; "
            "an object is an instance of that class. Define a class with 'class Name:', and use "
            "__init__ to set up initial attributes when an object is created. 'self' refers to the "
            "specific instance being worked with."
        ),
        "examples": (
            "class Student:\n"
            "    def __init__(self, name, course):\n"
            "        self.name = name\n"
            "        self.course = course\n"
            "\n"
            "    def introduce(self):\n"
            "        print(f\"I am {self.name}, studying {self.course}\")\n"
            "\n"
            "kabiru = Student(\"Kabiru\", \"Python\")\n"
            "kabiru.introduce()\n"
        ),
        "practice": (
            "1. Create a class Car with attributes brand and year\n"
            "2. Add a method describe() that prints the car's details\n"
            "3. Create two Car objects and call describe() on each"
        ),
        "mini_project": (
            "Mini Project: Student Record System\n"
            "Create a Student class with name, age, and a list of grades. Add a method average_grade() "
            "that returns the average. Create 3 students and print each one's average."
        ),
        "quiz": {
            "title": "Classes and Objects Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is a class in Python?",
                    "option_a": "A single value",
                    "option_b": "A blueprint for creating objects",
                    "option_c": "A type of loop",
                    "option_d": "A built-in function",
                    "correct_option": "b",
                    "explanation": "A class defines the structure and behavior that its objects will have.",
                },
                {
                    "text": "What does 'self' refer to inside a class method?",
                    "option_a": "The class itself",
                    "option_b": "The specific object instance calling the method",
                    "option_c": "A global variable",
                    "option_d": "Nothing, it's optional",
                    "correct_option": "b",
                    "explanation": "'self' represents the particular instance the method is being called on.",
                },
                {
                    "text": "Which method runs automatically when an object is created?",
                    "option_a": "__start__",
                    "option_b": "__init__",
                    "option_c": "__create__",
                    "option_d": "__new__",
                    "correct_option": "b",
                    "explanation": "__init__ is the constructor method, called automatically when an object is instantiated.",
                },
            ],
        },
    },
    {
        "slug": "python-17-inheritance",
        "title": "17. Inheritance and Polymorphism",
        "level": "intermediate",
        "explanation": (
            "Inheritance lets a class (child) reuse and extend another class's (parent) code. Write "
            "'class Child(Parent):' to inherit. Use super().__init__() to call the parent constructor. "
            "Polymorphism means different classes can define the same method name with different "
            "behavior, letting you treat different objects uniformly."
        ),
        "examples": (
            "class Animal:\n"
            "    def __init__(self, name):\n"
            "        self.name = name\n"
            "    def speak(self):\n"
            "        print(f\"{self.name} makes a sound\")\n"
            "\n"
            "class Dog(Animal):\n"
            "    def speak(self):\n"
            "        print(f\"{self.name} says Woof!\")\n"
            "\n"
            "animals = [Animal(\"Generic\"), Dog(\"Rex\")]\n"
            "for a in animals:\n"
            "    a.speak()\n"
        ),
        "practice": (
            "1. Create a base class Shape with a method area() that returns 0\n"
            "2. Create Circle and Square subclasses that override area() correctly\n"
            "3. Loop over a list of shapes and print each area()"
        ),
        "mini_project": (
            "Mini Project: Employee Management\n"
            "Create a base Employee class with name and salary. Create Manager and Developer subclasses "
            "that add extra attributes (team_size, programming_language) and override a describe() method."
        ),
        "quiz": {
            "title": "Inheritance Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does class Dog(Animal): mean?",
                    "option_a": "Dog is unrelated to Animal",
                    "option_b": "Dog inherits from Animal",
                    "option_c": "Animal inherits from Dog",
                    "option_d": "This is a syntax error",
                    "correct_option": "b",
                    "explanation": "Placing a class name in parentheses makes the new class inherit from it.",
                },
                {
                    "text": "What does super().__init__() do?",
                    "option_a": "Creates a new class",
                    "option_b": "Calls the parent class's constructor",
                    "option_c": "Deletes the parent class",
                    "option_d": "Nothing in Python 3",
                    "correct_option": "b",
                    "explanation": "super() gives access to the parent class, commonly used to call its __init__.",
                },
                {
                    "text": "What is polymorphism?",
                    "option_a": "Having many variables",
                    "option_b": "Different classes implementing the same method name differently",
                    "option_c": "A type of loop",
                    "option_d": "A file format",
                    "correct_option": "b",
                    "explanation": "Polymorphism allows objects of different classes to be used interchangeably via shared method names.",
                },
            ],
        },
    },
    {
        "slug": "python-18-comprehensions",
        "title": "18. List and Dictionary Comprehensions",
        "level": "intermediate",
        "explanation": (
            "Comprehensions offer a compact way to build lists, dictionaries, or sets from iterables. "
            "List comprehension: [expression for item in iterable if condition]. This is often faster "
            "and more readable than writing a full for loop with .append()."
        ),
        "examples": (
            "squares = [x ** 2 for x in range(10)]\n"
            "print(squares)\n"
            "\n"
            "evens = [x for x in range(20) if x % 2 == 0]\n"
            "print(evens)\n"
            "\n"
            "word_lengths = {word: len(word) for word in [\"hi\", \"python\", \"code\"]}\n"
            "print(word_lengths)\n"
        ),
        "practice": (
            "1. Use a list comprehension to create a list of cubes (n**3) from 1 to 10\n"
            "2. Use a list comprehension to filter only words longer than 4 letters from a list\n"
            "3. Use a dictionary comprehension to map numbers 1-5 to their squares"
        ),
        "mini_project": (
            "Mini Project: Grade Filter\n"
            "Given a list of student score dictionaries, use a list comprehension to build a new list "
            "containing only the names of students who scored 70 or above."
        ),
        "quiz": {
            "title": "Comprehensions Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does [x*2 for x in range(3)] produce?",
                    "option_a": "[0, 2, 4]",
                    "option_b": "[1, 2, 3]",
                    "option_c": "[2, 4, 6]",
                    "option_d": "[0, 1, 2]",
                    "correct_option": "a",
                    "explanation": "range(3) gives 0,1,2; doubling each gives [0, 2, 4].",
                },
                {
                    "text": "What is the main benefit of list comprehensions?",
                    "option_a": "They run on a different interpreter",
                    "option_b": "A compact, often more readable way to build lists",
                    "option_c": "They can only be used with numbers",
                    "option_d": "They replace functions entirely",
                    "correct_option": "b",
                    "explanation": "Comprehensions provide concise syntax for building collections from iterables.",
                },
                {
                    "text": "Which brackets create a dictionary comprehension?",
                    "option_a": "[]",
                    "option_b": "()",
                    "option_c": "{}",
                    "option_d": "<>",
                    "correct_option": "c",
                    "explanation": "Dictionary comprehensions use curly braces with a key:value expression.",
                },
            ],
        },
    },
    {
        "slug": "python-19-lambda-map-filter",
        "title": "19. Lambda Functions, map(), and filter()",
        "level": "intermediate",
        "explanation": (
            "A lambda is a small, anonymous function written in one line: lambda arguments: expression. "
            "map(function, iterable) applies a function to every item in an iterable. filter(function, "
            "iterable) keeps only items where the function returns True. Both are often used with lambdas."
        ),
        "examples": (
            "square = lambda x: x ** 2\n"
            "print(square(5))   # 25\n"
            "\n"
            "numbers = [1, 2, 3, 4, 5]\n"
            "doubled = list(map(lambda x: x * 2, numbers))\n"
            "print(doubled)     # [2, 4, 6, 8, 10]\n"
            "\n"
            "evens = list(filter(lambda x: x % 2 == 0, numbers))\n"
            "print(evens)       # [2, 4]\n"
        ),
        "practice": (
            "1. Write a lambda that adds 10 to a number\n"
            "2. Use map() with a lambda to convert a list of strings to uppercase\n"
            "3. Use filter() with a lambda to keep only numbers greater than 50 from a list"
        ),
        "mini_project": (
            "Mini Project: Price Discount Tool\n"
            "Given a list of prices, use map() with a lambda to apply a 10% discount to each price, "
            "then use filter() to show only discounted prices still above 1000."
        ),
        "quiz": {
            "title": "Lambda, map, filter Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How do you write a lambda that adds 1 to x?",
                    "option_a": "lambda x: x + 1",
                    "option_b": "lambda(x) x + 1",
                    "option_c": "def lambda x: x + 1",
                    "option_d": "lambda: x + 1",
                    "correct_option": "a",
                    "explanation": "The correct syntax is 'lambda arguments: expression'.",
                },
                {
                    "text": "What does map(func, iterable) do?",
                    "option_a": "Filters items out of the iterable",
                    "option_b": "Applies func to every item in the iterable",
                    "option_c": "Sorts the iterable",
                    "option_d": "Deletes the iterable",
                    "correct_option": "b",
                    "explanation": "map() applies a given function to each element of an iterable.",
                },
                {
                    "text": "What does filter(func, iterable) keep?",
                    "option_a": "Only items where func returns False",
                    "option_b": "Only items where func returns True",
                    "option_c": "All items unchanged",
                    "option_d": "Only the first item",
                    "correct_option": "b",
                    "explanation": "filter() keeps only the elements for which the function returns True.",
                },
            ],
        },
    },
    {
        "slug": "python-20-decorators",
        "title": "20. Decorators",
        "level": "advanced",
        "explanation": (
            "A decorator is a function that wraps another function to add extra behavior without "
            "changing its code. Decorators use the @decorator_name syntax placed above a function "
            "definition. They're commonly used for logging, timing, and access control."
        ),
        "examples": (
            "def log_call(func):\n"
            "    def wrapper(*args, **kwargs):\n"
            "        print(f\"Calling {func.__name__}\")\n"
            "        result = func(*args, **kwargs)\n"
            "        print(f\"Finished {func.__name__}\")\n"
            "        return result\n"
            "    return wrapper\n"
            "\n"
            "@log_call\n"
            "def greet(name):\n"
            "    print(f\"Hello, {name}!\")\n"
            "\n"
            "greet(\"Kabiru\")\n"
        ),
        "practice": (
            "1. Write a decorator that prints 'Starting...' before and 'Done!' after a function runs\n"
            "2. Apply your decorator to a function that adds two numbers\n"
            "3. Write a decorator that only allows a function to run if a condition (e.g. is_admin) is True"
        ),
        "mini_project": (
            "Mini Project: Timing Decorator\n"
            "Write a decorator called timer that measures and prints how long a function takes to run "
            "using the time module. Apply it to a function that does a large loop."
        ),
        "quiz": {
            "title": "Decorators Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What symbol is used to apply a decorator to a function?",
                    "option_a": "#",
                    "option_b": "@",
                    "option_c": "$",
                    "option_d": "&",
                    "correct_option": "b",
                    "explanation": "The @ symbol placed above a function definition applies a decorator.",
                },
                {
                    "text": "What is the main purpose of a decorator?",
                    "option_a": "To delete a function",
                    "option_b": "To add extra behavior to a function without changing its code",
                    "option_c": "To convert a function into a class",
                    "option_d": "To import a module",
                    "correct_option": "b",
                    "explanation": "Decorators wrap functions to extend their behavior cleanly and reusably.",
                },
                {
                    "text": "What does a decorator function typically return?",
                    "option_a": "A string",
                    "option_b": "A wrapper function",
                    "option_c": "None, always",
                    "option_d": "The original arguments",
                    "correct_option": "b",
                    "explanation": "Decorators return a new 'wrapper' function that calls the original with added behavior.",
                },
            ],
        },
    },
]
