import os

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.models import Course, Progress, Certificate, User
from app.schemas.content import CertificateOut
from app.services.certificate_gen import generate_certificate, render_certificate_pdf

router = APIRouter(prefix="/api/certificates", tags=["certificates"])


@router.get("", response_model=list[CertificateOut])
def list_certificates(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Certificate).filter(Certificate.user_id == current_user.id).all()


@router.post("/issue/{course_slug}", response_model=CertificateOut)
def issue_certificate(course_slug: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    course = db.query(Course).filter(Course.slug == course_slug).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    lesson_ids = [l.id for l in course.lessons]
    if not lesson_ids:
        raise HTTPException(status_code=400, detail="Course has no lessons yet")

    completed_ids = {
        p.lesson_id for p in
        db.query(Progress).filter(
            Progress.user_id == current_user.id,
            Progress.lesson_id.in_(lesson_ids),
            Progress.completed == True,
        ).all()
    }

    if len(completed_ids) < len(lesson_ids):
        raise HTTPException(
            status_code=400,
            detail=f"Course not yet complete: {len(completed_ids)}/{len(lesson_ids)} lessons done",
        )

    existing = db.query(Certificate).filter(
        Certificate.user_id == current_user.id, Certificate.course_id == course.id
    ).first()
    if existing:
        return existing

    code, filepath = generate_certificate(current_user.full_name, course.title)

    certificate = Certificate(
        user_id=current_user.id,
        course_id=course.id,
        certificate_code=code,
        file_path=filepath,
    )
    db.add(certificate)
    db.commit()
    db.refresh(certificate)
    return certificate


@router.get("/{certificate_id}/download")
def download_certificate(certificate_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cert = db.query(Certificate).filter(
        Certificate.id == certificate_id, Certificate.user_id == current_user.id
    ).first()
    if not cert:
        raise HTTPException(status_code=404, detail="Certificate not found")

    # Self-healing: the certificate RECORD lives in the database (persistent
    # once DATABASE_URL points at Postgres), but the PDF file itself lives on
    # local disk, which can still be wiped by a host restart. Rather than
    # 404-ing on an otherwise-valid, already-issued certificate, regenerate
    # the exact same PDF deterministically from its existing code.
    if not cert.file_path or not os.path.exists(cert.file_path):
        course = db.query(Course).filter(Course.id == cert.course_id).first()
        course_title = course.title if course else "Kabiru AI Tutor Course"
        new_path = render_certificate_pdf(current_user.full_name, course_title, cert.certificate_code)
        cert.file_path = new_path
        db.commit()
        db.refresh(cert)

    return FileResponse(cert.file_path, media_type="application/pdf", filename=f"{cert.certificate_code}.pdf")
