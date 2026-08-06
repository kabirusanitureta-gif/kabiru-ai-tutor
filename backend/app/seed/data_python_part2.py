"""
Seed data for the Python course — Part 2 (Lessons 6-10).
"""

PYTHON_LESSONS_PART2 = [
    {
        "slug": "python-06-lists",
        "title": "6. Lists",
        "level": "beginner",
        "explanation": (
            "A list is an ordered, changeable collection of items, written with square brackets. "
            "Lists can hold mixed types and can grow or shrink. Common methods: .append() adds an item, "
            ".remove() deletes a value, .pop() removes by index, .sort() orders items, and len() gives "
            "the number of items. You access items by index, starting at 0."
        ),
        "examples": (
            "fruits = [\"apple\", \"banana\", \"mango\"]\n"
            "fruits.append(\"orange\")\n"
            "print(fruits[0])       # 'apple'\n"
            "print(fruits[-1])      # 'orange' (last item)\n"
            "fruits.remove(\"banana\")\n"
            "print(len(fruits))     # 3\n"
        ),
        "practice": (
            "1. Create a list of 5 of your favorite foods\n"
            "2. Append one more food\n"
            "3. Remove the first food you added\n"
            "4. Print the final list and its length"
        ),
        "mini_project": (
            "Mini Project: Todo List Manager\n"
            "Create an empty list called tasks. Add 3 tasks with .append(). Print each task with its "
            "position number using a for loop and enumerate(). Then remove the second task and print "
            "the updated list."
        ),
        "quiz": {
            "title": "Lists Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What index does the first item in a list have?",
                    "option_a": "1",
                    "option_b": "0",
                    "option_c": "-1",
                    "option_d": "It depends on the list",
                    "correct_option": "b",
                    "explanation": "Python lists are zero-indexed — the first item is at index 0.",
                },
                {
                    "text": "Which method adds an item to the end of a list?",
                    "option_a": ".add()",
                    "option_b": ".append()",
                    "option_c": ".insert()",
                    "option_d": ".push()",
                    "correct_option": "b",
                    "explanation": ".append() adds a single item to the end of a list.",
                },
                {
                    "text": "What does fruits[-1] return?",
                    "option_a": "An error",
                    "option_b": "The first item",
                    "option_c": "The last item",
                    "option_d": "An empty list",
                    "correct_option": "c",
                    "explanation": "Negative indices count from the end; -1 is the last item.",
                },
            ],
        },
    },
    {
        "slug": "python-07-tuples-sets",
        "title": "7. Tuples and Sets",
        "level": "beginner",
        "explanation": (
            "A tuple is like a list but immutable — once created, its items cannot be changed. Tuples "
            "use parentheses: (1, 2, 3). They're useful for fixed collections of values, like coordinates. "
            "A set is an unordered collection of unique items, written with curly braces: {1, 2, 3}. "
            "Sets automatically remove duplicates and are useful for membership testing."
        ),
        "examples": (
            "point = (4, 5)\n"
            "print(point[0])   # 4\n"
            "\n"
            "numbers = {1, 2, 2, 3, 3, 3}\n"
            "print(numbers)    # {1, 2, 3}\n"
            "print(3 in numbers)  # True\n"
        ),
        "practice": (
            "1. Create a tuple with 3 colors\n"
            "2. Try to change one item and observe the error\n"
            "3. Create a set from a list with duplicate numbers and print the result"
        ),
        "mini_project": (
            "Mini Project: Unique Visitor Tracker\n"
            "Given a list of usernames with repeats, convert it to a set to find unique visitors, "
            "then print how many unique visitors there were."
        ),
        "quiz": {
            "title": "Tuples and Sets Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Can you change an item in a tuple after it's created?",
                    "option_a": "Yes, always",
                    "option_b": "No, tuples are immutable",
                    "option_c": "Only the first item",
                    "option_d": "Only if it's a number",
                    "correct_option": "b",
                    "explanation": "Tuples are immutable — their contents cannot be modified after creation.",
                },
                {
                    "text": "What symbol is used to create a set?",
                    "option_a": "[]",
                    "option_b": "()",
                    "option_c": "{}",
                    "option_d": "<>",
                    "correct_option": "c",
                    "explanation": "Sets use curly braces, e.g. {1, 2, 3}.",
                },
                {
                    "text": "Do sets allow duplicate values?",
                    "option_a": "Yes",
                    "option_b": "No",
                    "option_c": "Only strings",
                    "option_d": "Only numbers",
                    "correct_option": "b",
                    "explanation": "Sets automatically remove duplicate values, keeping only unique items.",
                },
            ],
        },
    },
    {
        "slug": "python-08-dictionaries",
        "title": "8. Dictionaries",
        "level": "beginner",
        "explanation": (
            "A dictionary stores data as key-value pairs, written with curly braces: {'key': 'value'}. "
            "You access values using their key, not a numeric index. Dictionaries are extremely useful "
            "for representing structured data, like a student's record. Use .keys(), .values(), and "
            ".items() to loop through a dictionary."
        ),
        "examples": (
            "student = {\"name\": \"Kabiru\", \"age\": 20, \"course\": \"Python\"}\n"
            "print(student[\"name\"])\n"
            "student[\"age\"] = 21\n"
            "for key, value in student.items():\n"
            "    print(key, \"->\", value)\n"
        ),
        "practice": (
            "1. Create a dictionary representing yourself with keys: name, age, city\n"
            "2. Update the age value\n"
            "3. Loop through the dictionary and print each key and value"
        ),
        "mini_project": (
            "Mini Project: Contact Book\n"
            "Create a dictionary of dictionaries representing 3 contacts, each with name and phone. "
            "Print each contact's info in a formatted line using a for loop."
        ),
        "quiz": {
            "title": "Dictionaries Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How do you access the value for key 'name' in dictionary student?",
                    "option_a": "student.name",
                    "option_b": "student['name']",
                    "option_c": "student(name)",
                    "option_d": "student->name",
                    "correct_option": "b",
                    "explanation": "Dictionary values are accessed using square brackets with the key.",
                },
                {
                    "text": "Which method returns both keys and values together?",
                    "option_a": ".keys()",
                    "option_b": ".values()",
                    "option_c": ".items()",
                    "option_d": ".pairs()",
                    "correct_option": "c",
                    "explanation": ".items() returns key-value pairs for iteration.",
                },
                {
                    "text": "What symbol separates a key from its value in a dictionary?",
                    "option_a": "=",
                    "option_b": "->",
                    "option_c": ":",
                    "option_d": ";",
                    "correct_option": "c",
                    "explanation": "Dictionaries use a colon to separate keys and values, e.g. 'key': 'value'.",
                },
            ],
        },
    },
    {
        "slug": "python-09-conditionals",
        "title": "9. Conditionals (if / elif / else)",
        "level": "beginner",
        "explanation": (
            "Conditionals let your program make decisions. 'if' runs a block only when a condition is "
            "True. 'elif' checks another condition if the first was False. 'else' runs when none of the "
            "above conditions were True. Indentation (4 spaces) defines which code belongs to each block."
        ),
        "examples": (
            "age = 18\n"
            "if age >= 18:\n"
            "    print(\"You are an adult\")\n"
            "elif age >= 13:\n"
            "    print(\"You are a teenager\")\n"
            "else:\n"
            "    print(\"You are a child\")\n"
        ),
        "practice": (
            "1. Write a program that checks if a number is positive, negative, or zero\n"
            "2. Write a program that checks if a student's score is >=70 (pass) or <70 (fail)\n"
            "3. Combine two conditions using 'and' in one if statement"
        ),
        "mini_project": (
            "Mini Project: Grade Calculator\n"
            "Given a score variable, print 'A' for 90+, 'B' for 80-89, 'C' for 70-79, 'D' for 60-69, "
            "and 'F' below 60, using if/elif/else."
        ),
        "quiz": {
            "title": "Conditionals Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What keyword checks an additional condition after 'if'?",
                    "option_a": "elseif",
                    "option_b": "elif",
                    "option_c": "then",
                    "option_d": "check",
                    "correct_option": "b",
                    "explanation": "Python uses 'elif' (short for else-if) to check further conditions.",
                },
                {
                    "text": "What defines a block of code inside an if statement in Python?",
                    "option_a": "Curly braces {}",
                    "option_b": "Indentation",
                    "option_c": "Semicolons",
                    "option_d": "Parentheses",
                    "correct_option": "b",
                    "explanation": "Python uses consistent indentation (commonly 4 spaces) to define code blocks.",
                },
                {
                    "text": "Which runs when none of the if/elif conditions are True?",
                    "option_a": "elif",
                    "option_b": "else",
                    "option_c": "default",
                    "option_d": "otherwise",
                    "correct_option": "b",
                    "explanation": "'else' is the fallback block that runs when no prior condition matched.",
                },
            ],
        },
    },
    {
        "slug": "python-10-loops",
        "title": "10. Loops (for / while)",
        "level": "beginner",
        "explanation": (
            "Loops repeat a block of code. A 'for' loop iterates over a sequence (list, string, range). "
            "A 'while' loop repeats as long as a condition stays True. Use 'break' to exit a loop early "
            "and 'continue' to skip to the next iteration. range(n) generates numbers from 0 to n-1."
        ),
        "examples": (
            "for i in range(5):\n"
            "    print(i)\n"
            "\n"
            "count = 0\n"
            "while count < 3:\n"
            "    print(\"Counting:\", count)\n"
            "    count += 1\n"
        ),
        "practice": (
            "1. Use a for loop to print numbers 1 to 10\n"
            "2. Use a while loop to print numbers 10 down to 1\n"
            "3. Use a for loop with 'continue' to print only even numbers from 0 to 20"
        ),
        "mini_project": (
            "Mini Project: Multiplication Table Generator\n"
            "Ask the user for a number, then use a for loop to print its multiplication table from "
            "1x to 12x."
        ),
        "quiz": {
            "title": "Loops Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does range(5) generate?",
                    "option_a": "1,2,3,4,5",
                    "option_b": "0,1,2,3,4",
                    "option_c": "0,1,2,3,4,5",
                    "option_d": "5,4,3,2,1",
                    "correct_option": "b",
                    "explanation": "range(5) produces numbers from 0 up to (but not including) 5.",
                },
                {
                    "text": "What keyword immediately exits a loop?",
                    "option_a": "stop",
                    "option_b": "exit",
                    "option_c": "break",
                    "option_d": "end",
                    "correct_option": "c",
                    "explanation": "'break' immediately terminates the nearest enclosing loop.",
                },
                {
                    "text": "What keyword skips to the next iteration of a loop?",
                    "option_a": "skip",
                    "option_b": "continue",
                    "option_c": "next",
                    "option_d": "pass",
                    "correct_option": "b",
                    "explanation": "'continue' skips the rest of the current iteration and moves to the next one.",
                },
            ],
        },
    },
]
