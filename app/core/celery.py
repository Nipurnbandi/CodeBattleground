from celery import Celery

celery_app = Celery(
    "codebattleground",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)


celery_app.conf.imports =("app.services.submission_worker",)