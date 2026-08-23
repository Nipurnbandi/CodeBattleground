import re
from datetime import datetime, timedelta, timezone

import bcrypt
from jose import JWTError, jwt

from app.core.config import settings


ALGORITHM = "HS256"


def is_password_strong(password: str) -> bool:
	return (
		len(password) >= 8
		and bool(re.search(r"[A-Z]", password))
		and bool(re.search(r"[a-z]", password))
		and bool(re.search(r"\d", password))
	)


def hash(password: str) -> str:
	return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify(password: str, hashed_password: str) -> bool:
	try:
		return bcrypt.checkpw(
			password.encode("utf-8"), hashed_password.encode("utf-8")
		)
	except (ValueError, TypeError):
		return False


def create_access_token(user_id: int) -> str:
	expires_at = datetime.now(timezone.utc) + timedelta(hours=settings.token_hours)
	payload = {"sub": str(user_id), "exp": expires_at}
	return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def decode_access_token(token: str) -> int | None:
	try:
		payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
		subject = payload.get("sub")
		return int(subject) if subject is not None else None
	except (JWTError, TypeError, ValueError):
		return None
