from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Participant(Base):
    __tablename__ = "participants"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    team_id = Column(String, ForeignKey("teams.id"))

    # Зв'язок з командою (опційно)
    team = relationship("Team", back_populates="participants")