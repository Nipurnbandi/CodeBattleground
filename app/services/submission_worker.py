from app.core.celery import celery_app
from app.core.database import SessionLocal
from app.models.problems import DefaultCodes, Problem
from app.models.submissions import Submission, SubmissionStatus
from app.models.users import Users


@celery_app.task
def execute_submission(submission_id: int):
    db = SessionLocal()

    try:
        submission=db.get(Submission, submission_id)

        if submission is None:
            print(f"Submission {submission_id} not found")
            return

        print(f"Processing submission {submission.id}")
        print(f"Code: {submission.source_code}")
        print(f"Language: {submission.language}")

        submission.status=SubmissionStatus.RUNNING
        db.commit()
    finally:
        db.close()