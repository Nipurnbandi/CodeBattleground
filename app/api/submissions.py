from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.submission_worker import execute_submission
from app.core.dependencies import get_current_user
from app.models.problems import Problem
from app.models.submissions import Submission
from app.models.users import Users
from app.schemas.schemas_submissions import SubmissionRequest, SubmissionResponse


router = APIRouter(prefix="/submissions", tags=["submissions"])


@router.post("/{problem_id}", response_model=SubmissionResponse, status_code=status.HTTP_201_CREATED)
async def create_submission(
	problem_id: int,
	request_model: SubmissionRequest,
	db: Session = Depends(get_db),
	current_user: Users = Depends(get_current_user),
):
	problem = db.query(Problem).filter(Problem.id==problem_id).first()
	if problem is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Problem not found")

	submission=Submission(
		user_id=current_user.id,
		problem_id=problem_id,
		language=request_model.language,
		source_code=request_model.source_code,
	)
	
	db.add(submission)
	db.commit()
	db.refresh(submission)
	execute_submission.delay(submission.id)
	return submission
