"""
Seed data for the FastAPI course — Part 3 (Lessons 11-15, final batch).
"""

FASTAPI_LESSONS_PART3 = [
    {
        "slug": "fastapi-11-file-uploads",
        "title": "11. File Uploads",
        "level": "advanced",
        "explanation": (
            "FastAPI handles file uploads using UploadFile from fastapi. It streams the file "
            "efficiently rather than loading it all into memory at once. Use 'file: UploadFile = "
            "File(...)' as a route parameter. Access file.filename, file.content_type, and read bytes "
            "with 'await file.read()'."
        ),
        "examples": (
            "from fastapi import UploadFile, File\n"
            "\n"
            "@app.post(\"/upload\")\n"
            "async def upload_file(file: UploadFile = File(...)):\n"
            "    contents = await file.read()\n"
            "    with open(f\"uploads/{file.filename}\", \"wb\") as f:\n"
            "        f.write(contents)\n"
            "    return {\"filename\": file.filename, \"size\": len(contents)}\n"
        ),
        "practice": (
            "1. Build a POST /upload route that accepts a file and saves it to disk\n"
            "2. Return the uploaded file's name and content type in the response\n"
            "3. Test uploading a file using the /docs interactive interface"
        ),
        "mini_project": (
            "Mini Project: Profile Picture Uploader\n"
            "Build a POST /users/{user_id}/avatar route that accepts an image UploadFile, validates "
            "that content_type starts with 'image/', saves it, and returns its saved path."
        ),
        "quiz": {
            "title": "File Uploads Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which FastAPI type handles file uploads efficiently?",
                    "option_a": "File",
                    "option_b": "UploadFile",
                    "option_c": "BinaryData",
                    "option_d": "FileObject",
                    "correct_option": "b",
                    "explanation": "UploadFile streams uploaded files efficiently without loading everything into memory at once.",
                },
                {
                    "text": "How do you read the bytes of an uploaded file?",
                    "option_a": "file.bytes",
                    "option_b": "await file.read()",
                    "option_c": "file.get_bytes()",
                    "option_d": "file.load()",
                    "correct_option": "b",
                    "explanation": "await file.read() asynchronously reads the uploaded file's content as bytes.",
                },
                {
                    "text": "Which attribute gives the uploaded file's original name?",
                    "option_a": "file.name",
                    "option_b": "file.filename",
                    "option_c": "file.title",
                    "option_d": "file.path",
                    "correct_option": "b",
                    "explanation": "UploadFile.filename holds the original filename sent by the client.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-12-background-tasks",
        "title": "12. Background Tasks",
        "level": "advanced",
        "explanation": (
            "BackgroundTasks let you run code AFTER returning a response to the client, useful for "
            "sending emails, writing logs, or other work that shouldn't delay the response. Add a "
            "BackgroundTasks parameter to your route, then call background_tasks.add_task(function, "
            "*args)."
        ),
        "examples": (
            "from fastapi import BackgroundTasks\n"
            "\n"
            "def write_log(message: str):\n"
            "    with open(\"log.txt\", \"a\") as f:\n"
            "        f.write(message + \"\\n\")\n"
            "\n"
            "@app.post(\"/notify\")\n"
            "def notify(background_tasks: BackgroundTasks):\n"
            "    background_tasks.add_task(write_log, \"Notification sent\")\n"
            "    return {\"message\": \"Notification is being processed\"}\n"
        ),
        "practice": (
            "1. Write a background task function that appends a line to a log file\n"
            "2. Trigger it from a route using BackgroundTasks.add_task()\n"
            "3. Confirm the response returns instantly while the log write happens after"
        ),
        "mini_project": (
            "Mini Project: Welcome Email Simulator\n"
            "Build a POST /register route that immediately returns 'Registered!' while a background "
            "task simulates sending a welcome email (e.g. sleeping 2 seconds then writing to a log file)."
        ),
        "quiz": {
            "title": "Background Tasks Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "When does a background task run relative to the response?",
                    "option_a": "Before the response is sent",
                    "option_b": "After the response has been sent to the client",
                    "option_c": "It blocks the response until finished",
                    "option_d": "Background tasks don't exist in FastAPI",
                    "correct_option": "b",
                    "explanation": "Background tasks execute after the response is returned, without delaying it.",
                },
                {
                    "text": "Which method schedules a background task?",
                    "option_a": "background_tasks.run()",
                    "option_b": "background_tasks.add_task()",
                    "option_c": "background_tasks.schedule()",
                    "option_d": "background_tasks.queue()",
                    "correct_option": "b",
                    "explanation": "add_task(function, *args, **kwargs) schedules a function to run in the background.",
                },
                {
                    "text": "What's a good use case for background tasks?",
                    "option_a": "Validating request data",
                    "option_b": "Sending a confirmation email after registration",
                    "option_c": "Authenticating the user",
                    "option_d": "Parsing the request body",
                    "correct_option": "b",
                    "explanation": "Background tasks suit work that shouldn't block the response, like emails or logging.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-13-testing",
        "title": "13. Testing FastAPI Applications",
        "level": "advanced",
        "explanation": (
            "FastAPI provides a TestClient (built on httpx) for writing automated tests without "
            "running a live server. Combine it with pytest or unittest to call your routes directly in "
            "tests and assert on status codes and response JSON, catching bugs before deployment."
        ),
        "examples": (
            "from fastapi.testclient import TestClient\n"
            "from main import app\n"
            "\n"
            "client = TestClient(app)\n"
            "\n"
            "def test_read_root():\n"
            "    response = client.get(\"/\")\n"
            "    assert response.status_code == 200\n"
            "    assert response.json() == {\"message\": \"Hello from FastAPI\"}\n"
        ),
        "practice": (
            "1. Write a test that checks GET / returns status 200\n"
            "2. Write a test that POSTs to a create route and checks the response contains the expected data\n"
            "3. Write a test that checks a protected route returns 401 without a token"
        ),
        "mini_project": (
            "Mini Project: Test Suite for Task API\n"
            "Using the Task API you built earlier, write a full pytest test file covering: creating a "
            "task, listing tasks, updating a task, deleting a task, and getting a 404 for a missing task."
        ),
        "quiz": {
            "title": "Testing FastAPI Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which class lets you test FastAPI routes without running a live server?",
                    "option_a": "MockClient",
                    "option_b": "TestClient",
                    "option_c": "APIClient",
                    "option_d": "RequestClient",
                    "correct_option": "b",
                    "explanation": "TestClient (from fastapi.testclient) simulates requests directly against your app.",
                },
                {
                    "text": "What must test function names typically start with for pytest to discover them?",
                    "option_a": "check_",
                    "option_b": "test_",
                    "option_c": "verify_",
                    "option_d": "run_",
                    "correct_option": "b",
                    "explanation": "pytest automatically discovers functions and files starting with 'test_'.",
                },
                {
                    "text": "Why write automated tests for an API?",
                    "option_a": "To make deployment slower",
                    "option_b": "To catch bugs automatically before they reach production",
                    "option_c": "It's required by Python syntax",
                    "option_d": "To replace documentation",
                    "correct_option": "b",
                    "explanation": "Automated tests verify behavior stays correct as code changes, catching regressions early.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-14-deployment",
        "title": "14. Deploying a FastAPI App",
        "level": "advanced",
        "explanation": (
            "To deploy FastAPI, you run it behind a production ASGI server like uvicorn (often with "
            "multiple workers via gunicorn). Common hosting options: Render, Railway, a VPS with "
            "Docker, or Termux for local/offline use. Always set environment variables (like "
            "SECRET_KEY) securely rather than hardcoding them, and never run with --reload in production."
        ),
        "examples": (
            "# Production run command (no --reload)\n"
            "uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4\n"
            "\n"
            "# Or with gunicorn managing uvicorn workers\n"
            "gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000\n"
        ),
        "practice": (
            "1. Run your FastAPI app with uvicorn using --host 0.0.0.0 so it's reachable on your network\n"
            "2. Move your SECRET_KEY into a .env file instead of hardcoding it\n"
            "3. Read about one hosting platform (Render or Railway) and note its free-tier deployment steps"
        ),
        "mini_project": (
            "Mini Project: Production-Ready Checklist\n"
            "Take an existing FastAPI project and prepare it for deployment: move all secrets to .env, "
            "add a requirements.txt, remove --reload from the run command, and write a short "
            "DEPLOYMENT.md describing how to start the app in production."
        ),
        "quiz": {
            "title": "Deployment Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Why should --reload be removed for production deployments?",
                    "option_a": "It's only a development convenience and adds overhead in production",
                    "option_b": "It disables the API entirely",
                    "option_c": "It's required for HTTPS",
                    "option_d": "It has no effect either way",
                    "correct_option": "a",
                    "explanation": "--reload watches files for changes, which is unnecessary overhead and risk in production.",
                },
                {
                    "text": "Where should sensitive values like SECRET_KEY be stored?",
                    "option_a": "Hardcoded directly in main.py",
                    "option_b": "In environment variables / a .env file, not committed to git",
                    "option_c": "In the frontend JavaScript code",
                    "option_d": "In the README",
                    "correct_option": "b",
                    "explanation": "Secrets belong in environment variables, kept out of source control for security.",
                },
                {
                    "text": "What is uvicorn's role in running a FastAPI app?",
                    "option_a": "It's the database engine",
                    "option_b": "It's the ASGI server that actually runs and serves the FastAPI app",
                    "option_c": "It's a testing framework",
                    "option_d": "It's a frontend build tool",
                    "correct_option": "b",
                    "explanation": "uvicorn is an ASGI server; it's what actually executes your FastAPI application and handles requests.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-15-final-project",
        "title": "15. Final Project: Complete REST API",
        "level": "advanced",
        "explanation": (
            "This capstone lesson combines everything: Pydantic models, SQLAlchemy database "
            "integration, JWT authentication, dependency injection, CRUD routes, error handling, and "
            "CORS. You'll build a small but complete 'Notes API' with real persistence and real auth — "
            "structurally very similar to how this Kabiru AI Tutor backend itself is built."
        ),
        "examples": (
            "# Structure recap for the final project:\n"
            "# app/main.py        -> creates the app, includes routers, sets up CORS\n"
            "# app/models.py      -> SQLAlchemy User and Note models\n"
            "# app/schemas.py     -> Pydantic request/response models\n"
            "# app/auth.py        -> register/login routes issuing JWTs\n"
            "# app/notes.py       -> protected CRUD routes for notes, scoped to current_user\n"
        ),
        "practice": (
            "1. Set up the folder structure above for a new mini project\n"
            "2. Implement register/login issuing JWTs, using bcrypt for password hashing\n"
            "3. Implement protected CRUD routes for 'notes' where a user only sees their own notes"
        ),
        "mini_project": (
            "Capstone Project: Personal Notes API\n"
            "Build a complete, secured REST API: users register and log in (JWT), then can create, "
            "list, update, and delete their own notes (title, content). Every notes route must require "
            "authentication and must only return/modify notes belonging to the requesting user. Add "
            "automated tests for at least the auth flow and one CRUD operation. This demonstrates full "
            "mastery of the FastAPI course."
        ),
        "quiz": {
            "title": "Final Project Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "In a secured notes API, why should notes routes filter by the current user's ID?",
                    "option_a": "To make queries slower",
                    "option_b": "So users can only see and modify their own data, not other users' data",
                    "option_c": "It's not necessary if JWT is used",
                    "option_d": "To reduce the database size",
                    "correct_option": "b",
                    "explanation": "Scoping queries to the authenticated user's ID is essential to prevent data leaks between users.",
                },
                {
                    "text": "What should be used to hash passwords before storing them?",
                    "option_a": "Store them as plain text for simplicity",
                    "option_b": "A secure hashing algorithm like bcrypt",
                    "option_c": "Base64 encoding",
                    "option_d": "Reversible encryption only",
                    "correct_option": "b",
                    "explanation": "bcrypt (via passlib) is a secure, salted hashing algorithm appropriate for password storage.",
                },
                {
                    "text": "Which dependency pattern ensures a route only runs for authenticated users?",
                    "option_a": "response_model",
                    "option_b": "current_user: User = Depends(get_current_user)",
                    "option_c": "status_code=200",
                    "option_d": "BackgroundTasks",
                    "correct_option": "b",
                    "explanation": "Depending on get_current_user forces token verification before the route body executes.",
                },
            ],
        },
    },
]
