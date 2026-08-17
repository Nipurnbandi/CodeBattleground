from app.core.database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,DateTime,Text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from typing import Optional
from sqlalchemy.orm import relationship


class Problems(Base):
    __tablename__="problems"
    id=Column(Integer,primary_key=True,nullable=False)
    slug=Column(String(100),nullable=False,unique=True)
    title=Column(String(250),nullable=False)
    statement_markdown=Column(Text,nullable=False)
    points=Column(Integer, nullable=False)
    time_limit_seconds=Column(Integer,nullable=False)
    memory_limit_mb=Column(Integer,nullable=False)
    created_at=Column(TIMESTAMP,server_default=text('now()'),nullable=False)
