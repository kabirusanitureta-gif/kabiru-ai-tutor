"""
Seed data for the FastAPI course — Part 1 (Lessons 1-5).
"""

FASTAPI_LESSONS_PART1 = [
    {
        "slug": "fastapi-01-introduction",
        "title": "1. Introduction to FastAPI",
        "level": "intermediate",
        "explanation": (
            "FastAPI is a modern Python web framework for building APIs quickly. It's fast (built on "
            "Starlette and Pydantic), has automatic interactive documentation (Swagger UI at /docs), "
            "and uses Python type hints for validation. It's used to build backends for web apps, "
            "mobile apps, and services like this very tutor platform."
        ),
        "examples": (
            "# main.py\n"
            "from fastapi import FastAPI\n"
            "\n"
            "app = FastAPI()\n"
            "\n"
            "@app.get(\"/\")\n"
            "def read_root():\n"
            "    return {\"message\": \"Hello from FastAPI\"}\n"
            "\n"
            "# Run with: uvicorn main:app --reload\n"
        ),
        "practice": (
            "1. Install FastAPI and uvicorn: pip install fastapi uvicorn\n"
            "2. Create the example app above and run it\n"
            "3. Visit http://127.0.0.1:8000/docs to see the automatic API documentation"
        ),
        "mini_project": (
            "Mini Project: Hello API\n"
            "Create a FastAPI app with 3 different GET routes: '/', '/about', and '/contact', each "
            "returning a different JSON message."
        ),
        "quiz": {
            "title": "Introduction to FastAPI Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does FastAPI use for automatic data validation?",
                    "option_a": "Regular expressions only",
                    "option_b": "Python type hints and Pydantic",
                    "option_c": "Manual if statements",
                    "option_d": "XML schemas",
                    "correct_option": "b",
                    "explanation": "FastAPI validates request data automatically based on Python type hints via Pydantic.",
                },
                {
                    "text": "Which command runs a FastAPI app during development?",
                    "option_a": "python main.py run",
                    "option_b": "uvicorn main:app --reload",
                    "option_c": "fastapi start main.py",
                    "option_d": "flask run main.py",
                    "correct_option": "b",
                    "explanation": "uvicorn is the ASGI server that runs FastAPI apps; --reload enables auto-restart on code changes.",
                },
                {
                    "text": "Where can you find FastAPI's automatic interactive API docs?",
                    "option_a": "/help",
                    "option_b": "/docs",
                    "option_c": "/api-docs",
                    "option_d": "/swagger",
                    "correct_option": "b",
                    "explanation": "FastAPI automatically serves Swagger UI documentation at the /docs endpoint.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-02-path-query-params",
        "title": "2. Path Parameters and Query Parameters",
        "level": "intermediate",
        "explanation": (
            "Path parameters are part of the URL itself, like /students/{student_id}. Query parameters "
            "come after a '?' in the URL, like /students?age=20. In FastAPI, you declare path "
            "parameters as function arguments matching the {curly braces}, and query parameters as "
            "regular function arguments with default values."
        ),
        "examples": (
            "@app.get(\"/students/{student_id}\")\n"
            "def get_student(student_id: int):\n"
            "    return {\"student_id\": student_id}\n"
            "\n"
            "@app.get(\"/students\")\n"
            "def list_students(min_age: int = 0, limit: int = 10):\n"
            "    return {\"min_age\": min_age, \"limit\": limit}\n"
            "\n"
            "# GET /students?min_age=18&limit=5\n"
        ),
        "practice": (
            "1. Create a route /books/{book_id} that returns the book_id as an int\n"
            "2. Create a route /search with query parameters q (string) and limit (int, default 10)\n"
            "3. Test both routes using the /docs interactive interface"
        ),
        "mini_project": (
            "Mini Project: Product Catalog API\n"
            "Build routes: GET /products/{product_id} (returns one product by ID) and GET /products "
            "with query parameters category and max_price to filter a hardcoded product list."
        ),
        "quiz": {
            "title": "Path and Query Parameters Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "In @app.get('/students/{student_id}'), what kind of parameter is student_id?",
                    "option_a": "Query parameter",
                    "option_b": "Path parameter",
                    "option_c": "Header parameter",
                    "option_d": "Body parameter",
                    "correct_option": "b",
                    "explanation": "Parameters inside curly braces in the route path are path parameters.",
                },
                {
                    "text": "How do query parameters appear in a URL?",
                    "option_a": "Inside curly braces in the path",
                    "option_b": "After a '?' as key=value pairs",
                    "option_c": "In the request body",
                    "option_d": "In the URL fragment after '#'",
                    "correct_option": "b",
                    "explanation": "Query parameters follow a '?' in the URL, e.g. ?min_age=18&limit=5.",
                },
                {
                    "text": "How does FastAPI know a function argument is a query parameter rather than a path parameter?",
                    "option_a": "It must be typed as str",
                    "option_b": "If it's not part of the route path pattern, FastAPI treats it as a query parameter",
                    "option_c": "You must add @query decorator",
                    "option_d": "Query parameters are impossible in FastAPI",
                    "correct_option": "b",
                    "explanation": "Any function parameter not matching a {placeholder} in the path is automatically a query parameter.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-03-request-body-pydantic",
        "title": "3. Request Body and Pydantic Models",
        "level": "intermediate",
        "explanation": (
            "For sending structured data (like a form), use a Pydantic model as the request body. "
            "Define a class inheriting from BaseModel with typed fields. FastAPI automatically parses "
            "and validates incoming JSON against this model, and returns clear error messages if the "
            "data doesn't match."
        ),
        "examples": (
            "from pydantic import BaseModel\n"
            "\n"
            "class Student(BaseModel):\n"
            "    name: str\n"
            "    age: int\n"
            "    email: str\n"
            "\n"
            "@app.post(\"/students\")\n"
            "def create_student(student: Student):\n"
            "    return {\"message\": f\"Created {student.name}\", \"data\": student}\n"
        ),
        "practice": (
            "1. Create a Pydantic model Book with title, author, and price fields\n"
            "2. Create a POST /books route that accepts a Book and returns a success message\n"
            "3. Test sending invalid data (e.g. missing a field) and observe FastAPI's error response"
        ),
        "mini_project": (
            "Mini Project: Feedback Collector API\n"
            "Create a Feedback Pydantic model (name, message, rating: int). Build a POST /feedback "
            "route that validates and stores submissions in an in-memory list, and a GET /feedback "
            "route that returns all collected feedback."
        ),
        "quiz": {
            "title": "Request Body and Pydantic Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which base class do Pydantic models inherit from?",
                    "option_a": "Model",
                    "option_b": "BaseModel",
                    "option_c": "Schema",
                    "option_d": "DataModel",
                    "correct_option": "b",
                    "explanation": "Pydantic request/response models inherit from pydantic.BaseModel.",
                },
                {
                    "text": "What happens if incoming JSON doesn't match a Pydantic model's required fields?",
                    "option_a": "FastAPI silently ignores the mismatch",
                    "option_b": "FastAPI returns a validation error automatically",
                    "option_c": "The server crashes",
                    "option_d": "The fields are set to None without warning",
                    "correct_option": "b",
                    "explanation": "FastAPI automatically returns a 422 error describing exactly what validation failed.",
                },
                {
                    "text": "In def create_student(student: Student):, where does FastAPI get 'student' from?",
                    "option_a": "The URL path",
                    "option_b": "The query string",
                    "option_c": "The JSON request body",
                    "option_d": "Environment variables",
                    "correct_option": "c",
                    "explanation": "A Pydantic model type-hinted parameter is parsed from the JSON request body by default.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-04-response-models-status",
        "title": "4. Response Models and Status Codes",
        "level": "intermediate",
        "explanation": (
            "You can specify a response_model in a route decorator to control exactly what data is "
            "returned (and hide sensitive fields like passwords). Use status_code to set the HTTP "
            "response code, e.g. 201 for created, 204 for no content. FastAPI's Response models also "
            "power the auto-generated documentation."
        ),
        "examples": (
            "from pydantic import BaseModel\n"
            "\n"
            "class StudentOut(BaseModel):\n"
            "    name: str\n"
            "    age: int\n"
            "\n"
            "@app.post(\"/students\", response_model=StudentOut, status_code=201)\n"
            "def create_student(student: Student):\n"
            "    return student   # password or internal fields would be filtered out automatically\n"
        ),
        "practice": (
            "1. Create a UserOut model that excludes a password field present in the input model\n"
            "2. Set status_code=201 on a creation route\n"
            "3. Test that the response never leaks the password field, even if you return the full object"
        ),
        "mini_project": (
            "Mini Project: Safe User API\n"
            "Create UserIn (with password) and UserOut (without password) models. Build a POST /users "
            "route with response_model=UserOut and status_code=201 that confirms passwords never leak "
            "in the response."
        ),
        "quiz": {
            "title": "Response Models and Status Codes Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is the purpose of response_model in a route decorator?",
                    "option_a": "To validate incoming requests only",
                    "option_b": "To control and filter exactly what data is returned to the client",
                    "option_c": "To set the database schema",
                    "option_d": "To rename the route",
                    "correct_option": "b",
                    "explanation": "response_model shapes and filters the outgoing response, hiding fields not defined on it.",
                },
                {
                    "text": "Which HTTP status code conventionally means 'successfully created'?",
                    "option_a": "200",
                    "option_b": "201",
                    "option_c": "204",
                    "option_d": "301",
                    "correct_option": "b",
                    "explanation": "201 Created is the standard status code for successful resource creation.",
                },
                {
                    "text": "Why separate UserIn and UserOut models?",
                    "option_a": "FastAPI requires two models for every route",
                    "option_b": "To prevent sensitive input fields like passwords from appearing in responses",
                    "option_c": "It makes the code run faster",
                    "option_d": "There's no real reason, it's just convention",
                    "correct_option": "b",
                    "explanation": "Separate input/output models let you accept sensitive data while never echoing it back.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-05-crud-routes",
        "title": "5. Building CRUD Routes (GET, POST, PUT, DELETE)",
        "level": "intermediate",
        "explanation": (
            "CRUD stands for Create, Read, Update, Delete — the four basic data operations. In "
            "FastAPI/REST convention: POST creates, GET reads, PUT (or PATCH) updates, DELETE removes. "
            "Combining these on a resource path (e.g. /items and /items/{id}) forms a complete API for "
            "managing that resource."
        ),
        "examples": (
            "items = {}\n"
            "\n"
            "@app.post(\"/items/{item_id}\")\n"
            "def create_item(item_id: int, name: str):\n"
            "    items[item_id] = name\n"
            "    return {\"created\": item_id}\n"
            "\n"
            "@app.get(\"/items/{item_id}\")\n"
            "def read_item(item_id: int):\n"
            "    return {\"item\": items.get(item_id)}\n"
            "\n"
            "@app.put(\"/items/{item_id}\")\n"
            "def update_item(item_id: int, name: str):\n"
            "    items[item_id] = name\n"
            "    return {\"updated\": item_id}\n"
            "\n"
            "@app.delete(\"/items/{item_id}\")\n"
            "def delete_item(item_id: int):\n"
            "    items.pop(item_id, None)\n"
            "    return {\"deleted\": item_id}\n"
        ),
        "practice": (
            "1. Build a full CRUD API for a 'notes' resource using an in-memory dictionary\n"
            "2. Add proper status codes (201 for create, 204 for delete)\n"
            "3. Test all 4 operations from the /docs interface"
        ),
        "mini_project": (
            "Mini Project: Task API\n"
            "Build a complete CRUD API for tasks (id, title, done) stored in memory: POST /tasks, "
            "GET /tasks, GET /tasks/{id}, PUT /tasks/{id}, DELETE /tasks/{id}. Return 404 for a "
            "missing task ID using HTTPException."
        ),
        "quiz": {
            "title": "CRUD Routes Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which HTTP method conventionally creates a new resource?",
                    "option_a": "GET",
                    "option_b": "POST",
                    "option_c": "DELETE",
                    "option_d": "OPTIONS",
                    "correct_option": "b",
                    "explanation": "POST is the standard method for creating a new resource.",
                },
                {
                    "text": "Which HTTP method conventionally updates an existing resource fully?",
                    "option_a": "GET",
                    "option_b": "PUT",
                    "option_c": "POST",
                    "option_d": "HEAD",
                    "correct_option": "b",
                    "explanation": "PUT is conventionally used to replace/update an existing resource.",
                },
                {
                    "text": "What does CRUD stand for?",
                    "option_a": "Create, Read, Update, Delete",
                    "option_b": "Copy, Retrieve, Undo, Discard",
                    "option_c": "Connect, Request, Upload, Download",
                    "option_d": "Create, Run, Undo, Debug",
                    "correct_option": "a",
                    "explanation": "CRUD is the acronym for the four fundamental data operations.",
                },
            ],
        },
    },
]
