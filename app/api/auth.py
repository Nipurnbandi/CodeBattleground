from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core import security
from app.models.users import Users
from app.schemas.schemas_auth import (
    LoginRequest,
    TokenResponse,
    UsersRequest,
    UsersResponse,
)


router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UsersResponse)
async def register(request_model: UsersRequest, db: Session = Depends(get_db)):
    email = request_model.email.strip().lower()

    existing_user = db.query(Users).filter(
        (Users.email == email) | (Users.username == request_model.username)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already registered"
        )

    if not security.is_password_strong(request_model.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please provide a strong password"
        )

    hashed_password = security.hash(request_model.password)

    new_user = Users(
        username=request_model.username,
        email=email,
        password=hashed_password
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already registered"
        )

    return new_user


@router.post("/login", response_model=TokenResponse)
async def login(request_model: LoginRequest, db: Session = Depends(get_db)):
    email = request_model.email.strip().lower()
    user = db.query(Users).filter(Users.email == email).first()

    if user is None or not security.verify(request_model.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return TokenResponse(access_token=security.create_access_token(user.id))
