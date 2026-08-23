import enum
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class SubmissionStatus(str, enum.Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    AC = "AC"
    WA = "WA"
    TLE = "TLE"
    MLE = "MLE"
    RE = "RE"
    CE = "CE"


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    problem_id = Column(Integer, ForeignKey("problem.id"), index=True)
    language = Column(String(16))
    source_code = Column(Text)
    status = Column(Enum(SubmissionStatus),default=SubmissionStatus.PENDING,index=True)
    tests_total = Column(Integer, default=0)
    tests_done = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True),server_default=func.now())