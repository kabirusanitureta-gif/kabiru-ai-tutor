"""
Generates a PDF certificate when a student completes all lessons in a course.
Uses reportlab (pure Python, works on Termux/Pydroid/Linux/Windows).

Split into two functions so a certificate can be regenerated on-demand from
its existing code if the underlying file was lost (e.g. Render/Railway's
ephemeral filesystem wiping local files on restart, even though the DB
record itself persists in Postgres).
"""
import os
import uuid
from datetime import datetime

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

CERT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "certificates")
os.makedirs(CERT_DIR, exist_ok=True)


def render_certificate_pdf(student_name: str, course_title: str, code: str) -> str:
    """
    Renders (or re-renders) the certificate PDF for a given, already-issued
    certificate code, writing it to a deterministic path based on the code.
    Safe to call multiple times — always produces the same file for the same
    code, so it can be used both for initial generation and for self-healing
    re-generation if the file was lost.
    """
    filename = f"{code}.pdf"
    filepath = os.path.join(CERT_DIR, filename)

    c = canvas.Canvas(filepath, pagesize=landscape(A4))
    width, height = landscape(A4)

    c.setFillColor(HexColor("#0f172a"))
    c.rect(0, 0, width, height, fill=True, stroke=False)

    c.setStrokeColor(HexColor("#22c55e"))
    c.setLineWidth(6)
    c.rect(1 * cm, 1 * cm, width - 2 * cm, height - 2 * cm, stroke=True, fill=False)

    c.setFillColor(HexColor("#f8fafc"))
    c.setFont("Helvetica-Bold", 34)
    c.drawCentredString(width / 2, height - 4 * cm, "KABIRU AI TUTOR")

    c.setFont("Helvetica", 18)
    c.drawCentredString(width / 2, height - 5.2 * cm, "Certificate of Completion")

    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2, height - 7 * cm, "This certifies that")

    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(HexColor("#22c55e"))
    c.drawCentredString(width / 2, height - 8.3 * cm, student_name)

    c.setFillColor(HexColor("#f8fafc"))
    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2, height - 9.6 * cm, "has successfully completed the course")

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 10.8 * cm, course_title)

    c.setFont("Helvetica", 11)
    c.drawCentredString(width / 2, 2.5 * cm, f"Issued: {datetime.utcnow().strftime('%Y-%m-%d')}  |  Certificate ID: {code}")

    c.showPage()
    c.save()

    return filepath


def generate_certificate(student_name: str, course_title: str) -> tuple[str, str]:
    """Issues a brand-new certificate: generates a fresh code and renders its PDF.
    Returns (certificate_code, absolute_file_path)."""
    code = f"KAT-{uuid.uuid4().hex[:10].upper()}"
    filepath = render_certificate_pdf(student_name, course_title, code)
    return code, filepath
