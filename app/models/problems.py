from app.core.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Text,UniqueConstraint
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class Problem(Base):
    __tablename__="problem"

    id=Column(Integer,primary_key=True,nullable=False)
    slug=Column(String(100),nullable=False,unique=True)
    title=Column(String(250),nullable=False)
    statement_markdown=Column(Text,nullable=False)
    points=Column(Integer,nullable=False)
    time_limit_seconds=Column(Integer,nullable=False)
    memory_limit_mb=Column(Integer,nullable=False)
    created_at=Column(TIMESTAMP,server_default=text("now()"),nullable=False)

    default_codes=relationship("DefaultCodes",back_populates="problem")


class DefaultCodes(Base):
    __tablename__="default_codes"

    __table_args__=(UniqueConstraint("problem_id","language"),)

    id=Column(Integer,primary_key=True,nullable=False)
    problem_id=Column(Integer,ForeignKey("problem.id",ondelete="CASCADE"),nullable=False)
    language=Column(String(10),nullable=False)
    starter_code=Column(Text,nullable=False)
    full_boilerplate=Column(Text,nullable=False)

    problem=relationship("Problem",back_populates="default_codes")