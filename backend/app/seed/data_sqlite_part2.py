"""
Seed data for the SQLite course — Part 2 (Lessons 6-10, final batch).
"""

SQLITE_LESSONS_PART2 = [
    {
        "slug": "sqlite-06-sorting-filtering",
        "title": "6. Sorting and Filtering (ORDER BY, LIMIT)",
        "level": "beginner",
        "explanation": (
            "ORDER BY sorts query results by one or more columns, ascending (ASC, default) or "
            "descending (DESC). LIMIT restricts how many rows are returned — useful for pagination or "
            "getting just the top results. You can combine ORDER BY, WHERE, and LIMIT in one query."
        ),
        "examples": (
            "cursor.execute(\"SELECT * FROM students ORDER BY age DESC\")\n"
            "print(cursor.fetchall())\n"
            "\n"
            "cursor.execute(\"SELECT * FROM students ORDER BY name ASC LIMIT 5\")\n"
            "print(cursor.fetchall())\n"
            "\n"
            "cursor.execute(\"SELECT * FROM students WHERE age > 18 ORDER BY age LIMIT 3\")\n"
            "print(cursor.fetchall())\n"
        ),
        "practice": (
            "1. Query all students ordered by age from oldest to youngest\n"
            "2. Query the top 3 youngest students using ORDER BY and LIMIT\n"
            "3. Combine WHERE, ORDER BY, and LIMIT in a single query"
        ),
        "mini_project": (
            "Mini Project: Leaderboard\n"
            "Create a scores table (id, player_name, score). Insert 10 sample rows, then write a query "
            "that returns the top 5 highest scores, ordered from highest to lowest."
        ),
        "quiz": {
            "title": "Sorting and Filtering Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which clause sorts query results?",
                    "option_a": "SORT BY",
                    "option_b": "ORDER BY",
                    "option_c": "ARRANGE BY",
                    "option_d": "GROUP BY",
                    "correct_option": "b",
                    "explanation": "ORDER BY sorts rows by the specified column(s).",
                },
                {
                    "text": "What does DESC mean in ORDER BY age DESC?",
                    "option_a": "Sort ascending",
                    "option_b": "Sort descending (highest to lowest)",
                    "option_c": "Delete the column",
                    "option_d": "Describe the table",
                    "correct_option": "b",
                    "explanation": "DESC sorts results from highest to lowest value.",
                },
                {
                    "text": "Which clause limits the number of rows returned?",
                    "option_a": "TOP",
                    "option_b": "LIMIT",
                    "option_c": "MAX",
                    "option_d": "ROWCOUNT",
                    "correct_option": "b",
                    "explanation": "LIMIT n restricts a query to return at most n rows.",
                },
            ],
        },
    },
    {
        "slug": "sqlite-07-aggregate-functions",
        "title": "7. Aggregate Functions (COUNT, SUM, AVG, MIN, MAX)",
        "level": "intermediate",
        "explanation": (
            "Aggregate functions calculate a single value from many rows. COUNT() counts rows, SUM() "
            "totals a numeric column, AVG() computes the average, MIN()/MAX() find the smallest/largest "
            "value. Use GROUP BY to calculate aggregates per category, e.g. average score per class."
        ),
        "examples": (
            "cursor.execute(\"SELECT COUNT(*) FROM students\")\n"
            "print(cursor.fetchone())    # (total_count,)\n"
            "\n"
            "cursor.execute(\"SELECT AVG(age) FROM students\")\n"
            "print(cursor.fetchone())\n"
            "\n"
            "cursor.execute(\"SELECT course, COUNT(*) FROM enrollments GROUP BY course\")\n"
            "print(cursor.fetchall())\n"
        ),
        "practice": (
            "1. Count the total number of students\n"
            "2. Find the average age of all students\n"
            "3. Use GROUP BY to count students per course in an enrollments table"
        ),
        "mini_project": (
            "Mini Project: Sales Report\n"
            "Create an orders table (id, product, amount). Insert sample orders, then write queries "
            "that show total revenue (SUM), average order value (AVG), and order count per product "
            "(GROUP BY)."
        ),
        "quiz": {
            "title": "Aggregate Functions Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which function counts the number of rows?",
                    "option_a": "SUM()",
                    "option_b": "COUNT()",
                    "option_c": "TOTAL()",
                    "option_d": "NUM()",
                    "correct_option": "b",
                    "explanation": "COUNT() returns the number of rows matching a query.",
                },
                {
                    "text": "Which clause groups rows to calculate aggregates per category?",
                    "option_a": "GROUP BY",
                    "option_b": "ORDER BY",
                    "option_c": "CATEGORY BY",
                    "option_d": "SET BY",
                    "correct_option": "a",
                    "explanation": "GROUP BY groups rows sharing a value so aggregates apply per group.",
                },
                {
                    "text": "Which function calculates the average of a numeric column?",
                    "option_a": "MEAN()",
                    "option_b": "AVG()",
                    "option_c": "MID()",
                    "option_d": "AVERAGE()",
                    "correct_option": "b",
                    "explanation": "AVG() computes the arithmetic mean of a numeric column.",
                },
            ],
        },
    },
    {
        "slug": "sqlite-08-joins",
        "title": "8. Joins",
        "level": "intermediate",
        "explanation": (
            "Joins combine rows from two or more tables based on a related column, avoiding duplicate "
            "data. INNER JOIN returns rows that match in both tables. LEFT JOIN returns all rows from "
            "the left table, with NULLs where there's no match in the right table. Joins are essential "
            "for relational database design."
        ),
        "examples": (
            "cursor.execute(\"\"\"\n"
            "SELECT students.name, enrollments.course\n"
            "FROM students\n"
            "INNER JOIN enrollments ON students.id = enrollments.student_id\n"
            "\"\"\")\n"
            "print(cursor.fetchall())\n"
            "\n"
            "cursor.execute(\"\"\"\n"
            "SELECT students.name, enrollments.course\n"
            "FROM students\n"
            "LEFT JOIN enrollments ON students.id = enrollments.student_id\n"
            "\"\"\")\n"
            "print(cursor.fetchall())\n"
        ),
        "practice": (
            "1. Create students and enrollments tables linked by student_id\n"
            "2. Write an INNER JOIN query showing each student's enrolled course\n"
            "3. Write a LEFT JOIN query that also shows students with NO enrollments"
        ),
        "mini_project": (
            "Mini Project: Course Enrollment Report\n"
            "Design students, courses, and enrollments tables (many-to-many via enrollments). Write a "
            "JOIN query that lists every student alongside every course they're enrolled in, with "
            "student and course names (not just IDs)."
        ),
        "quiz": {
            "title": "Joins Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does INNER JOIN return?",
                    "option_a": "All rows from both tables regardless of match",
                    "option_b": "Only rows that match in both tables",
                    "option_c": "Only rows from the left table",
                    "option_d": "Random rows",
                    "correct_option": "b",
                    "explanation": "INNER JOIN returns only rows where the join condition matches in both tables.",
                },
                {
                    "text": "What does LEFT JOIN guarantee?",
                    "option_a": "All rows from the right table, matched or not",
                    "option_b": "All rows from the left table, matched or not (NULL if no match)",
                    "option_c": "Only matched rows",
                    "option_d": "It deletes unmatched rows",
                    "correct_option": "b",
                    "explanation": "LEFT JOIN keeps every row from the left table, filling unmatched columns with NULL.",
                },
                {
                    "text": "What is typically used to link two tables in a JOIN?",
                    "option_a": "A shared column like a foreign key (e.g. student_id)",
                    "option_b": "The table names must match exactly",
                    "option_c": "Column order",
                    "option_d": "The number of rows",
                    "correct_option": "a",
                    "explanation": "Joins connect tables using a shared key, typically a foreign key relationship.",
                },
            ],
        },
    },
    {
        "slug": "sqlite-09-indexes",
        "title": "9. Indexes and Performance",
        "level": "advanced",
        "explanation": (
            "An index speeds up searches on a column, similar to a book's index. Without indexes, "
            "SQLite scans every row (a 'full table scan') to find matches, which is slow on large "
            "tables. Create one with CREATE INDEX. Indexes speed up SELECT/WHERE/ORDER BY but slightly "
            "slow down INSERT/UPDATE since the index must also update."
        ),
        "examples": (
            "cursor.execute(\"CREATE INDEX IF NOT EXISTS idx_students_name ON students(name)\")\n"
            "conn.commit()\n"
            "\n"
            "# Now searches by name are much faster on large tables:\n"
            "cursor.execute(\"SELECT * FROM students WHERE name = ?\", (\"Kabiru\",))\n"
            "print(cursor.fetchall())\n"
        ),
        "practice": (
            "1. Create an index on the age column of the students table\n"
            "2. Use EXPLAIN QUERY PLAN before a SELECT to see if the index is used\n"
            "3. Research: why shouldn't you index every single column?"
        ),
        "mini_project": (
            "Mini Project: Query Optimization Exercise\n"
            "Create a table with 1000+ generated rows using a loop. Time a WHERE query before and after "
            "adding an index on the filtered column, and print both durations to compare."
        ),
        "quiz": {
            "title": "Indexes and Performance Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is the main benefit of an index?",
                    "option_a": "It reduces file size",
                    "option_b": "It speeds up searches on a column",
                    "option_c": "It encrypts the data",
                    "option_d": "It creates backups automatically",
                    "correct_option": "b",
                    "explanation": "Indexes let SQLite find matching rows quickly instead of scanning the whole table.",
                },
                {
                    "text": "What is a downside of adding too many indexes?",
                    "option_a": "Nothing, more is always better",
                    "option_b": "INSERT/UPDATE operations become slower because indexes must update too",
                    "option_c": "SELECT queries become slower",
                    "option_d": "The database becomes read-only",
                    "correct_option": "b",
                    "explanation": "Every index adds overhead to write operations since it must stay in sync with the table.",
                },
                {
                    "text": "Which statement creates an index?",
                    "option_a": "CREATE INDEX",
                    "option_b": "ADD INDEX",
                    "option_c": "NEW INDEX",
                    "option_d": "MAKE INDEX",
                    "correct_option": "a",
                    "explanation": "CREATE INDEX index_name ON table(column) creates a new index.",
                },
            ],
        },
    },
    {
        "slug": "sqlite-10-python-transactions",
        "title": "10. Using SQLite with Python: Transactions and Best Practices",
        "level": "advanced",
        "explanation": (
            "A transaction groups multiple operations so they all succeed or all fail together, keeping "
            "data consistent. If an error occurs mid-transaction, call conn.rollback() to undo all "
            "changes since the last commit. Best practices: always use parameterized queries, close "
            "connections properly (or use 'with sqlite3.connect(...) as conn:'), and wrap risky "
            "operations in try/except with rollback on failure."
        ),
        "examples": (
            "import sqlite3\n"
            "\n"
            "conn = sqlite3.connect(\"bank.db\")\n"
            "cursor = conn.cursor()\n"
            "\n"
            "try:\n"
            "    cursor.execute(\"UPDATE accounts SET balance = balance - 100 WHERE id = 1\")\n"
            "    cursor.execute(\"UPDATE accounts SET balance = balance + 100 WHERE id = 2\")\n"
            "    conn.commit()\n"
            "    print(\"Transfer successful\")\n"
            "except Exception as e:\n"
            "    conn.rollback()\n"
            "    print(f\"Transfer failed, rolled back: {e}\")\n"
            "finally:\n"
            "    conn.close()\n"
        ),
        "practice": (
            "1. Write a two-step transaction (e.g. transferring money between two rows)\n"
            "2. Intentionally cause an error in the middle and confirm rollback() undoes both changes\n"
            "3. Refactor your connection code to use 'with sqlite3.connect(...) as conn:'"
        ),
        "mini_project": (
            "Capstone Project: Mini Banking System\n"
            "Build a small SQLite-backed app with an accounts table (id, owner, balance). Implement a "
            "transfer(from_id, to_id, amount) function using a transaction: it must check sufficient "
            "balance, perform both updates atomically, and roll back safely on any failure."
        ),
        "quiz": {
            "title": "Transactions and Best Practices Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does conn.rollback() do?",
                    "option_a": "Saves all changes permanently",
                    "option_b": "Undoes all changes made since the last commit",
                    "option_c": "Closes the database",
                    "option_d": "Deletes the database file",
                    "correct_option": "b",
                    "explanation": "rollback() reverts uncommitted changes, restoring the database to its last committed state.",
                },
                {
                    "text": "Why group related operations into a single transaction?",
                    "option_a": "To make queries run in parallel",
                    "option_b": "So they all succeed together or all fail together, keeping data consistent",
                    "option_c": "It's required syntax in SQLite",
                    "option_d": "To reduce file size",
                    "correct_option": "b",
                    "explanation": "Transactions ensure atomicity — partial, inconsistent updates are avoided.",
                },
                {
                    "text": "What is a key security best practice when writing SQL queries with user input?",
                    "option_a": "Concatenate user input directly into the SQL string",
                    "option_b": "Always use parameterized queries with ? placeholders",
                    "option_c": "Disable the database",
                    "option_d": "Only use SELECT statements",
                    "correct_option": "b",
                    "explanation": "Parameterized queries prevent SQL injection by safely separating code from data.",
                },
            ],
        },
    },
]
