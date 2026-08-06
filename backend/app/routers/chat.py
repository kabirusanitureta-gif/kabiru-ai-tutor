from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.models import ChatMessage, User
from app.schemas.content import ChatIn, ChatOut, CodeCheckIn, CodeCheckOut
from app.services.ai_tutor import get_tutor_reply, explain_error
from app.services.code_checker import check_python_code

router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.post("", response_model=ChatOut)
def chat(payload: ChatIn, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    reply, language = get_tutor_reply(payload.message, current_user.preferred_language)

    db.add(ChatMessage(user_id=current_user.id, role="user", content=payload.message, language=language))
    db.add(ChatMessage(user_id=current_user.id, role="assistant", content=reply, language=language))
    db.commit()

    return ChatOut(reply=reply, language=language)


@router.get("/history")
def chat_history(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == current_user.id)
        .order_by(ChatMessage.created_at.asc())
        .limit(200)
        .all()
    )
    return [
        {"role": m.role, "content": m.content, "language": m.language, "created_at": m.created_at}
        for m in messages
    ]


@router.post("/explain-error")
def explain_error_endpoint(payload: ChatIn, current_user: User = Depends(get_current_user)):
    language = current_user.preferred_language if current_user.preferred_language in ("en", "ha") else "en"
    explanation_en = explain_error(payload.message, "en")
    explanation_ha = explain_error(payload.message, "ha")
    return {"explanation_en": explanation_en, "explanation_ha": explanation_ha, "preferred": language}


@router.post("/check-code", response_model=CodeCheckOut)
def check_code(payload: CodeCheckIn, current_user: User = Depends(get_current_user)):
    result = check_python_code(payload.code)
    return CodeCheckOut(**result)
