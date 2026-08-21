from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.schemas_problems import ProblemResponse, ProblemDetailResponse
from app.core.database import get_db
from app.models.problems import Problem

router = APIRouter(
    prefix="/problems",
    tags=["problems"]
)


@router.get("", response_model=list[ProblemResponse])
async def problems(db: Session = Depends(get_db)):
    data = db.query(Problem).all()

    if not data:
        raise HTTPException(status_code=404, detail="Problems not found")

    return data


@router.get("/{slug}", response_model=ProblemDetailResponse)
async def problem_detail(slug: str, db: Session = Depends(get_db)):
    data = db.query(Problem).filter(Problem.slug == slug).first()

    if data is None:
        raise HTTPException(status_code=404, detail="Problem not found")

    return data