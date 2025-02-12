from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.participant import Participant
from app.database import SessionLocal
from pydantic import BaseModel

router = APIRouter()

# Pydantic модель для валідації запитів
class ParticipantCreate(BaseModel):
    name: str
    age: int
    team_id: str | None = None

# Dependency для отримання сесії БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/participants/", response_model=ParticipantCreate)
def create_participant(participant: ParticipantCreate, db: Session = Depends(get_db)):
    db_participant = Participant(**participant.dict())
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant

@router.get("/participants/{participant_id}")
def get_participant(participant_id: str, db: Session = Depends(get_db)):
    participant = db.query(Participant).filter(Participant.id == participant_id).first()
    if not participant:
        raise HTTPException(status_code=404, detail="Participant not found")
    return participant