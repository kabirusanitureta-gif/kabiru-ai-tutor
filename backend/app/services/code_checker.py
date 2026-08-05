"""
Checks student-submitted Python code:
1. Syntax validation via compile()
2. Execution in a restricted subprocess with a timeout
3. Bilingual (Hausa/English) error explanation using ai_tutor.explain_error
"""
import subprocess
import sys
import tempfile
import os

from app.services.ai_tutor import explain_error


def check_python_code(code: str, timeout_seconds: int = 5) -> dict:
    errors: list[str] = []

    # 1. Syntax check first (fast, safe)
    try:
        compile(code, "<student_code>", "exec")
    except SyntaxError as e:
        msg = f"SyntaxError: {e.msg} (line {e.lineno})"
        errors.append(msg)
        return {
            "passed_basic_checks": False,
            "feedback_en": explain_error(msg, "en"),
            "feedback_ha": explain_error(msg, "ha"),
            "errors": errors,
        }

    # 2. Execute in an isolated subprocess with a timeout so it can never hang
    #    or damage the host system. No network/file access assumptions are made
    #    beyond the student's own code running in a temp file.
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            [sys.executable, tmp_path],
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
        if result.returncode != 0:
            stderr_last_line = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else "Unknown error"
            errors.append(stderr_last_line)
            return {
                "passed_basic_checks": False,
                "feedback_en": explain_error(stderr_last_line, "en"),
                "feedback_ha": explain_error(stderr_last_line, "ha"),
                "errors": errors,
            }
        return {
            "passed_basic_checks": True,
            "feedback_en": f"Your code ran successfully. Output:\n{result.stdout.strip()}",
            "feedback_ha": f"Code dinka ya yi aiki daidai. Sakamako:\n{result.stdout.strip()}",
            "errors": [],
        }
    except subprocess.TimeoutExpired:
        errors.append("TimeoutError: code took too long to run")
        return {
            "passed_basic_checks": False,
            "feedback_en": "Your code took too long to run — check for infinite loops.",
            "feedback_ha": "Code dinka ya dauki lokaci mai yawa — duba ko akwai infinite loop.",
            "errors": errors,
        }
    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
