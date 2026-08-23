from sqlalchemy import Column, Integer, String, TIMESTAMP
from app.core.database import Base
from sqlalchemy.sql.expression import text


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    rating = Column(Integer, unique=False)
    max_rating = Column(Integer, unique=False)
    created_at = Column(TIMESTAMP, server_default=text("now()"), nullable=False)

