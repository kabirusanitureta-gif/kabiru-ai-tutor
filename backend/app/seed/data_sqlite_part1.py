"""
Seed data for the SQLite course — Part 1 (Lessons 1-5).
"""

SQLITE_LESSONS_PART1 = [
    {
        "slug": "sqlite-01-introduction",
        "title": "1. Introduction to Databases and SQLite",
        "level": "beginner",
        "explanation": (
            "A database stores structured data so it can be efficiently saved, searched, and updated. "
            "SQLite is a lightweight, file-based database engine built into Python — no server "
            "installation needed. It stores everything in a single .db file, making it perfect for "
            "small apps, prototypes, and offline tools like this tutor."
        ),
        "examples": (
            "import sqlite3\n"
            "\n"
            "# Connect to (or create) a database file\n"
            "conn = sqlite3.connect(\"school.db\")\n"
            "cursor = conn.cursor()\n"
            "print(\"Connected to SQLite database!\")\n"
            "conn.close()\n"
        ),
        "practice": (
            "1. Install Python's sqlite3 module check (it's built-in, just import it)\n"
            "2. Create a connection to a new file called test.db\n"
            "3. Print the sqlite3.version to confirm it works"
        ),
        "mini_project": (
            "Mini Project: Database Connection Checker\n"
            "Write a script that connects to a database file, prints a success message with the "
            "filename, and safely closes the connection using try/finally."
        ),
        "quiz": {
            "title": "Introduction to SQLite Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What type of database is SQLite?",
                    "option_a": "A cloud-only database",
                    "option_b": "A lightweight, file-based database engine",
                    "option_c": "A NoSQL document store",
                    "option_d": "A spreadsheet program",
                    "correct_option": "b",
                    "explanation": "SQLite stores all data in a single local file and needs no separate server.",
                },
                {
                    "text": "Which Python module is used to work with SQLite?",
                    "option_a": "sql",
                    "option_b": "sqlite3",
                    "option_c": "db",
                    "option_d": "pysql",
                    "correct_option": "b",
                    "explanation": "sqlite3 is Python's built-in module for SQLite databases.",
                },
                {
                    "text": "Which function opens a connection to an SQLite database file?",
                    "option_a": "sqlite3.open()",
                    "option_b": "sqlite3.connect()",
                    "option_c": "sqlite3.link()",
                    "option_d": "sqlite3.start()",
                    "correct_option": "b",
                    "explanation": "sqlite3.connect('file.db') opens (or creates) a connection to the database file.",
                },
            ],
        },
    },
    {
        "slug": "sqlite-02-creating-tables",
        "title": "2. Creating Tables",
        "level": "beginner",
        "explanation": (
            "A table organizes data into rows and columns, like a spreadsheet. You define a table's "
            "structure with SQL's CREATE TABLE statement, specifying column names and data types "
            "(INTEGER, TEXT, REAL, BLOB). The PRIMARY KEY uniquely identifies each row, often an "
            "auto-incrementing id."
        ),
        "examples": (
            "import sqlite3\n"
            "conn = sqlite3.connect(\"school.db\")\n"
            "cursor = conn.cursor()\n"
            "\n"
            "cursor.execute(\"\"\"\n"
            "CREATE TABLE IF NOT EXISTS students (\n"
            "    id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
            "    name TEXT NOT NULL,\n"
            "    age INTEGER\n"
            ")\n"
            "\"\"\")\n"
            "conn.commit()\n"
            "conn.close()\n"
        ),
        "practice": (
            "1. Create a table called books with columns id, title, author\n"
            "2. Add a price REAL column to the books table\n"
            "3. Run the script twice and confirm 'IF NOT EXISTS' prevents an error on the second run"
        ),
        "mini_project": (
            "Mini Project: Library Schema\n"
            "Design and create two tables: books (id, title, author, available) and members (id, name, "
            "email). Use appropriate data types and a PRIMARY KEY for each."
        ),
        "quiz": {
            "title": "Creating Tables Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which SQL statement creates a new table?",
                    "option_a": "NEW TABLE",
                    "option_b": "MAKE TABLE",
                    "option_c": "CREATE TABLE",
                    "option_d": "BUILD TABLE",
                    "correct_option": "c",
                    "explanation": "CREATE TABLE is the standard SQL statement for defining a new table.",
                },
                {
                    "text": "What does PRIMARY KEY do for a column?",
                    "option_a": "Makes it optional",
                    "option_b": "Uniquely identifies each row in the table",
                    "option_c": "Encrypts the column",
                    "option_d": "Deletes duplicate rows automatically",
                    "correct_option": "b",
                    "explanation": "A PRIMARY KEY uniquely identifies every row and cannot repeat or be null.",
                },
                {
                    "text": "Which data type would you use for storing decimal prices in SQLite?",
                    "option_a": "TEXT",
                    "option_b": "INTEGER",
                    "option_c": "REAL",
                    "option_d": "BLOB",
                    "correct_option": "c",
                    "explanation": "REAL stores floating-point (decimal) numbers in SQLite.",
                },
            ],
        },
    },
    {
        "slug": "sqlite-03-inserting-data",
        "title": "3. Inserting Data",
        "level": "beginner",
        "explanation": (
            "INSERT INTO adds new rows to a table. Always use parameterized queries (with ? "
            "placeholders) instead of putting variables directly into SQL strings — this prevents SQL "
            "injection attacks and handles special characters safely. Don't forget conn.commit() to "
            "save your changes."
        ),
        "examples": (
            "cursor.execute(\n"
            "    \"INSERT INTO students (name, age) VALUES (?, ?)\",\n"
            "    (\"Kabiru\", 20)\n"
            ")\n"
            "conn.commit()\n"
            "\n"
            "# Insert multiple rows at once\n"
            "students = [(\"Amina\", 19), (\"Musa\", 22)]\n"
            "cursor.executemany(\"INSERT INTO students (name, age) VALUES (?, ?)\", students)\n"
            "conn.commit()\n"
        ),
        "practice": (
            "1. Insert 3 students into your students table using parameterized queries\n"
            "2. Use executemany() to insert a list of 5 books at once\n"
            "3. Confirm the inserts worked by checking cursor.rowcount"
        ),
        "mini_project": (
            "Mini Project: Bulk Data Loader\n"
            "Create a list of 10 sample student records (name, age tuples) and insert them all into the "
            "database using executemany(), then commit the transaction."
        ),
        "quiz": {
            "title": "Inserting Data Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Why use ? placeholders instead of embedding variables directly in SQL strings?",
                    "option_a": "It's faster to type",
                    "option_b": "It prevents SQL injection and handles special characters safely",
                    "option_c": "It's required by Python syntax",
                    "option_d": "It makes queries run in parallel",
                    "correct_option": "b",
                    "explanation": "Parameterized queries protect against SQL injection attacks.",
                },
                {
                    "text": "What must you call to save changes after an INSERT?",
                    "option_a": "conn.save()",
                    "option_b": "conn.commit()",
                    "option_c": "cursor.finish()",
                    "option_d": "conn.write()",
                    "correct_option": "b",
                    "explanation": "conn.commit() writes pending changes permanently to the database file.",
                },
                {
                    "text": "Which method inserts many rows efficiently in one call?",
                    "option_a": "cursor.executemany()",
                    "option_b": "cursor.insertall()",
                    "option_c": "cursor.bulk_insert()",
                    "option_d": "cursor.multi_execute()",
                    "correct_option": "a",
                    "explanation": "executemany() runs the same INSERT statement for a list of parameter tuples.",
                },
            ],
        },
    },
    {
        "slug": "sqlite-04-querying-data",
        "title": "4. Querying Data (SELECT and WHERE)",
        "level": "beginner",
        "explanation": (
            "SELECT retrieves data from a table. Use WHERE to filter rows by a condition. "
            "cursor.fetchall() returns all matching rows as a list of tuples, fetchone() returns just "
            "one row, and fetchmany(n) returns n rows. SELECT * gets all columns, or list specific "
            "column names."
        ),
        "examples": (
            "cursor.execute(\"SELECT * FROM students WHERE age > ?\", (18,))\n"
            "rows = cursor.fetchall()\n"
            "for row in rows:\n"
            "    print(row)\n"
            "\n"
            "cursor.execute(\"SELECT name FROM students WHERE name = ?\", (\"Kabiru\",))\n"
            "result = cursor.fetchone()\n"
            "print(result)\n"
        ),
        "practice": (
            "1. Write a query that selects all students older than 20\n"
            "2. Write a query that selects only the name column for all rows\n"
            "3. Use fetchone() to get a single specific student by name"
        ),
        "mini_project": (
            "Mini Project: Student Search Tool\n"
            "Write a function search_students(min_age) that queries and prints all students at or "
            "above a given age, formatted neatly."
        ),
        "quiz": {
            "title": "Querying Data Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which SQL keyword filters rows based on a condition?",
                    "option_a": "FILTER",
                    "option_b": "WHERE",
                    "option_c": "IF",
                    "option_d": "HAVING",
                    "correct_option": "b",
                    "explanation": "WHERE restricts a query's results to rows matching a condition.",
                },
                {
                    "text": "Which method retrieves ALL matching rows from a query?",
                    "option_a": "cursor.fetchone()",
                    "option_b": "cursor.fetchall()",
                    "option_c": "cursor.getall()",
                    "option_d": "cursor.selectall()",
                    "correct_option": "b",
                    "explanation": "fetchall() returns every row matched by the last executed query.",
                },
                {
                    "text": "What does SELECT * FROM students mean?",
                    "option_a": "Select only the first row",
                    "option_b": "Select all columns from the students table",
                    "option_c": "Delete all students",
                    "option_d": "Count all students",
                    "correct_option": "b",
                    "explanation": "The * wildcard selects every column in the table.",
                },
            ],
        },
    },
    {
        "slug": "sqlite-05-update-delete",
        "title": "5. Updating and Deleting Data",
        "level": "beginner",
        "explanation": (
            "UPDATE modifies existing rows; DELETE removes rows. Both should almost always be paired "
            "with a WHERE clause — without one, they affect EVERY row in the table, which is a common "
            "and dangerous mistake. Always commit() after making changes."
        ),
        "examples": (
            "cursor.execute(\n"
            "    \"UPDATE students SET age = ? WHERE name = ?\",\n"
            "    (21, \"Kabiru\")\n"
            ")\n"
            "conn.commit()\n"
            "\n"
            "cursor.execute(\"DELETE FROM students WHERE name = ?\", (\"Musa\",))\n"
            "conn.commit()\n"
            "print(f\"Rows affected: {cursor.rowcount}\")\n"
        ),
        "practice": (
            "1. Update a student's age using an UPDATE statement with WHERE\n"
            "2. Delete one specific student by id using DELETE with WHERE\n"
            "3. Try running UPDATE without a WHERE clause on a test table and observe that ALL rows change"
        ),
        "mini_project": (
            "Mini Project: Inventory Manager\n"
            "Create a products table (id, name, quantity). Write update_stock(product_id, new_quantity) "
            "and remove_product(product_id) functions using parameterized UPDATE and DELETE statements."
        ),
        "quiz": {
            "title": "Update and Delete Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What happens if you run UPDATE students SET age = 20 without a WHERE clause?",
                    "option_a": "Nothing happens",
                    "option_b": "Only the first row updates",
                    "option_c": "EVERY row in the table gets age set to 20",
                    "option_d": "It raises a syntax error",
                    "correct_option": "c",
                    "explanation": "Without WHERE, UPDATE and DELETE apply to all rows in the table — a common costly mistake.",
                },
                {
                    "text": "Which statement removes rows from a table?",
                    "option_a": "REMOVE",
                    "option_b": "DELETE",
                    "option_c": "DROP",
                    "option_d": "CLEAR",
                    "correct_option": "b",
                    "explanation": "DELETE FROM table WHERE condition removes matching rows (DROP removes the whole table).",
                },
                {
                    "text": "What does cursor.rowcount show after an UPDATE or DELETE?",
                    "option_a": "The total rows in the table",
                    "option_b": "The number of rows affected by the last statement",
                    "option_c": "The number of columns",
                    "option_d": "Always zero",
                    "correct_option": "b",
                    "explanation": "rowcount reports how many rows were changed by the most recent operation.",
                },
            ],
        },
    },
]
