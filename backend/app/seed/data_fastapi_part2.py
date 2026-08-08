"""
Seed data for the FastAPI course — Part 2 (Lessons 6-10).
"""

FASTAPI_LESSONS_PART2 = [
    {
        "slug": "fastapi-06-dependency-injection",
        "title": "6. Dependency Injection",
        "level": "advanced",
        "explanation": (
            "Dependency Injection lets you share reusable logic (like getting a DB session, checking "
            "authentication, or pagination parameters) across routes cleanly. Define a function, then "
            "use Depends(function) as a route parameter — FastAPI calls it automatically and passes "
            "the result to your route. This is exactly how Kabiru AI Tutor shares its get_db and "
            "get_current_user logic across dozens of routes."
        ),
        "examples": (
            "from fastapi import Depends\n"
            "\n"
            "def get_query_params(skip: int = 0, limit: int = 10):\n"
            "    return {\"skip\": skip, \"limit\": limit}\n"
            "\n"
            "@app.get(\"/items\")\n"
            "def list_items(params: dict = Depends(get_query_params)):\n"
            "    return params\n"
        ),
        "practice": (
            "1. Write a dependency function that returns a fixed 'fake_db' dictionary\n"
            "2. Use Depends() to inject it into two different routes\n"
            "3. Write a dependency that raises an HTTPException if a fake 'token' query parameter is missing"
        ),
        "mini_project": (
            "Mini Project: Reusable Pagination\n"
            "Write a get_pagination(page: int = 1, page_size: int = 10) dependency and use Depends() "
            "to apply it consistently across 3 different list routes (users, products, orders)."
        ),
        "quiz": {
            "title": "Dependency Injection Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does Depends() do in a FastAPI route?",
                    "option_a": "Blocks the route from running",
                    "option_b": "Tells FastAPI to call another function and inject its result as a parameter",
                    "option_c": "Imports a Python package",
                    "option_d": "Deletes a dependency",
                    "correct_option": "b",
                    "explanation": "Depends(func) tells FastAPI to run func and pass its return value into the route.",
                },
                {
                    "text": "Why is dependency injection useful?",
                    "option_a": "It makes routes run in parallel automatically",
                    "option_b": "It lets you reuse logic like DB sessions or auth checks across many routes",
                    "option_c": "It's required for every FastAPI route",
                    "option_d": "It replaces Pydantic models",
                    "correct_option": "b",
                    "explanation": "Dependencies centralize shared logic so you don't repeat it in every route.",
                },
                {
                    "text": "In this tutor's codebase, what dependency provides the logged-in user to a route?",
                    "option_a": "get_db",
                    "option_b": "get_current_user",
                    "option_c": "get_settings",
                    "option_d": "get_token",
                    "correct_option": "b",
                    "explanation": "get_current_user (in core/deps.py) decodes the JWT and returns the authenticated User.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-07-database-sqlalchemy",
        "title": "7. Database Integration with SQLAlchemy",
        "level": "advanced",
        "explanation": (
            "SQLAlchemy is Python's most popular ORM (Object-Relational Mapper) — it lets you define "
            "database tables as Python classes and query them with Python instead of raw SQL. FastAPI "
            "apps typically create an 'engine', a 'SessionLocal' factory, and a get_db() dependency "
            "that yields a session per request and closes it afterward — exactly the pattern used in "
            "this tutor's core/database.py."
        ),
        "examples": (
            "from sqlalchemy.orm import Session\n"
            "from fastapi import Depends\n"
            "\n"
            "def get_db():\n"
            "    db = SessionLocal()\n"
            "    try:\n"
            "        yield db\n"
            "    finally:\n"
            "        db.close()\n"
            "\n"
            "@app.get(\"/students\")\n"
            "def list_students(db: Session = Depends(get_db)):\n"
            "    return db.query(Student).all()\n"
        ),
        "practice": (
            "1. Define a simple SQLAlchemy model with 3 columns\n"
            "2. Write a get_db() dependency generator function\n"
            "3. Write a route that queries all rows of your model using db.query(Model).all()"
        ),
        "mini_project": (
            "Mini Project: Book Catalog API\n"
            "Define a Book SQLAlchemy model (id, title, author). Create GET /books and POST /books "
            "routes using db: Session = Depends(get_db), committing new books to a real SQLite file."
        ),
        "quiz": {
            "title": "SQLAlchemy Integration Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does ORM stand for?",
                    "option_a": "Object-Relational Mapping",
                    "option_b": "Online Resource Manager",
                    "option_c": "Ordered Record Model",
                    "option_d": "Object Request Middleware",
                    "correct_option": "a",
                    "explanation": "ORM (Object-Relational Mapping) lets you work with database tables as Python classes.",
                },
                {
                    "text": "Why does get_db() use 'yield' instead of 'return'?",
                    "option_a": "yield is required syntax in FastAPI",
                    "option_b": "So code after yield (closing the session) runs after the request finishes",
                    "option_c": "yield makes queries run faster",
                    "option_d": "There's no real reason",
                    "correct_option": "b",
                    "explanation": "Using yield makes get_db a generator dependency — FastAPI runs the cleanup (db.close()) after the request completes.",
                },
                {
                    "text": "What method typically retrieves all rows for a SQLAlchemy model?",
                    "option_a": "db.query(Model).all()",
                    "option_b": "db.select(Model)",
                    "option_c": "Model.get_all()",
                    "option_d": "db.fetch(Model)",
                    "correct_option": "a",
                    "explanation": "db.query(Model).all() is the standard SQLAlchemy ORM call to fetch every row.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-08-jwt-authentication",
        "title": "8. Authentication with JWT",
        "level": "advanced",
        "explanation": (
            "JWT (JSON Web Token) is a compact, signed token used to prove a user's identity without "
            "storing sessions server-side. On login, the server creates a token containing the user's "
            "ID, signed with a secret key. The client sends this token in the Authorization header on "
            "future requests; the server verifies the signature to trust the request."
        ),
        "examples": (
            "from jose import jwt\n"
            "from datetime import datetime, timedelta\n"
            "\n"
            "SECRET_KEY = \"your-secret-key\"\n"
            "\n"
            "def create_access_token(data: dict):\n"
            "    to_encode = data.copy()\n"
            "    to_encode[\"exp\"] = datetime.utcnow() + timedelta(hours=24)\n"
            "    return jwt.encode(to_encode, SECRET_KEY, algorithm=\"HS256\")\n"
            "\n"
            "token = create_access_token({\"sub\": \"1\"})\n"
            "print(token)\n"
        ),
        "practice": (
            "1. Generate a JWT for a fake user id using jose.jwt.encode()\n"
            "2. Decode it back using jwt.decode() and print the payload\n"
            "3. Try decoding with the WRONG secret key and observe the error"
        ),
        "mini_project": (
            "Mini Project: Mini Login System\n"
            "Build a hardcoded-user login route that returns a JWT on correct username/password, and a "
            "protected /me route that requires a valid Bearer token (using OAuth2PasswordBearer + "
            "Depends) to return the username."
        ),
        "quiz": {
            "title": "JWT Authentication Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does JWT stand for?",
                    "option_a": "Java Web Token",
                    "option_b": "JSON Web Token",
                    "option_c": "JavaScript Web Transfer",
                    "option_d": "Joint Web Ticket",
                    "correct_option": "b",
                    "explanation": "JWT (JSON Web Token) is a signed, URL-safe token format for representing claims.",
                },
                {
                    "text": "Where does a client typically send its JWT on subsequent requests?",
                    "option_a": "In the URL path",
                    "option_b": "In the Authorization header as a Bearer token",
                    "option_c": "In a cookie only",
                    "option_d": "It's not sent again",
                    "correct_option": "b",
                    "explanation": "The standard pattern is 'Authorization: Bearer <token>' on each authenticated request.",
                },
                {
                    "text": "Why is the SECRET_KEY important for JWTs?",
                    "option_a": "It encrypts the token so no one can read it",
                    "option_b": "It's used to sign and verify the token, proving it wasn't tampered with",
                    "option_c": "It's only used for logging",
                    "option_d": "It has no real purpose",
                    "correct_option": "b",
                    "explanation": "The secret key signs the token; anyone without it cannot forge a valid token.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-09-middleware-cors",
        "title": "9. Middleware and CORS",
        "level": "advanced",
        "explanation": (
            "Middleware runs code before/after every request, useful for logging, timing, or modifying "
            "responses globally. CORS (Cross-Origin Resource Sharing) controls which frontend origins "
            "(domains) are allowed to call your API from a browser. Without CORSMiddleware configured "
            "correctly, a React frontend on a different port/domain will be blocked by the browser."
        ),
        "examples": (
            "from fastapi.middleware.cors import CORSMiddleware\n"
            "\n"
            "app.add_middleware(\n"
            "    CORSMiddleware,\n"
            "    allow_origins=[\"http://localhost:5173\"],\n"
            "    allow_credentials=True,\n"
            "    allow_methods=[\"*\"],\n"
            "    allow_headers=[\"*\"],\n"
            ")\n"
            "\n"
            "@app.middleware(\"http\")\n"
            "async def log_requests(request, call_next):\n"
            "    print(f\"Request: {request.method} {request.url}\")\n"
            "    response = await call_next(request)\n"
            "    return response\n"
        ),
        "practice": (
            "1. Add CORSMiddleware to a FastAPI app allowing your frontend's origin\n"
            "2. Write a custom middleware that logs how long each request takes\n"
            "3. Test that a request from a disallowed origin is blocked by the browser"
        ),
        "mini_project": (
            "Mini Project: Request Timing Middleware\n"
            "Write a custom middleware that measures each request's duration and adds it as a custom "
            "response header called X-Process-Time."
        ),
        "quiz": {
            "title": "Middleware and CORS Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What problem does CORS configuration solve?",
                    "option_a": "It speeds up database queries",
                    "option_b": "It allows a frontend on a different origin to call your API from the browser",
                    "option_c": "It encrypts all traffic",
                    "option_d": "It compresses responses",
                    "correct_option": "b",
                    "explanation": "CORS controls whether browsers permit cross-origin requests from a given frontend domain.",
                },
                {
                    "text": "What does middleware run relative to your route handlers?",
                    "option_a": "Only after the response is sent",
                    "option_b": "Before and/or after every request passes through",
                    "option_c": "Only once when the server starts",
                    "option_d": "Never automatically",
                    "correct_option": "b",
                    "explanation": "Middleware wraps every request/response cycle, running custom logic around your routes.",
                },
                {
                    "text": "If allow_origins=['http://localhost:5173'], what happens to a request from a different origin?",
                    "option_a": "It's always allowed",
                    "option_b": "The browser blocks it based on the CORS policy",
                    "option_c": "The server crashes",
                    "option_d": "It's redirected automatically",
                    "correct_option": "b",
                    "explanation": "Browsers enforce CORS policies client-side, blocking disallowed cross-origin requests.",
                },
            ],
        },
    },
    {
        "slug": "fastapi-10-error-handling",
        "title": "10. Error Handling and Exception Handlers",
        "level": "advanced",
        "explanation": (
            "Use HTTPException to return proper error responses with a status code and message, e.g. "
            "raise HTTPException(status_code=404, detail='Not found'). For custom error types across "
            "your whole app, define a custom exception handler with @app.exception_handler(). This "
            "keeps error responses consistent instead of leaking raw Python tracebacks to users."
        ),
        "examples": (
            "from fastapi import HTTPException\n"
            "\n"
            "@app.get(\"/students/{student_id}\")\n"
            "def get_student(student_id: int):\n"
            "    student = fake_db.get(student_id)\n"
            "    if not student:\n"
            "        raise HTTPException(status_code=404, detail=\"Student not found\")\n"
            "    return student\n"
            "\n"
            "from fastapi.responses import JSONResponse\n"
            "from fastapi import Request\n"
            "\n"
            "@app.exception_handler(ValueError)\n"
            "def value_error_handler(request: Request, exc: ValueError):\n"
            "    return JSONResponse(status_code=400, content={\"detail\": str(exc)})\n"
        ),
        "practice": (
            "1. Add a 404 HTTPException to a route when a requested item isn't found\n"
            "2. Add a 400 HTTPException when invalid input is detected (e.g. negative quantity)\n"
            "3. Write a custom exception_handler for a custom Python exception class"
        ),
        "mini_project": (
            "Mini Project: Robust Inventory API\n"
            "Build an inventory API where GET /items/{id} returns 404 for unknown IDs, and a custom "
            "OutOfStockError exception is raised and handled globally with a clean 409 JSON response."
        ),
        "quiz": {
            "title": "Error Handling Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which class is used to return a proper HTTP error response in FastAPI?",
                    "option_a": "HTTPError",
                    "option_b": "HTTPException",
                    "option_c": "APIError",
                    "option_d": "ResponseError",
                    "correct_option": "b",
                    "explanation": "raise HTTPException(status_code=..., detail=...) is FastAPI's standard error mechanism.",
                },
                {
                    "text": "What status code conventionally means 'resource not found'?",
                    "option_a": "400",
                    "option_b": "401",
                    "option_c": "404",
                    "option_d": "500",
                    "correct_option": "c",
                    "explanation": "404 Not Found is the standard status code for a missing resource.",
                },
                {
                    "text": "What is the purpose of a custom @app.exception_handler()?",
                    "option_a": "To catch and format a specific exception type consistently across the whole app",
                    "option_b": "To disable all error handling",
                    "option_c": "To slow down error responses",
                    "option_d": "It only works for HTTPException",
                    "correct_option": "a",
                    "explanation": "Custom exception handlers centralize how a given exception type is converted to a response.",
                },
            ],
        },
    },
]
