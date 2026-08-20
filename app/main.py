from fastapi import FastAPI
from .api import problems
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def test():
    return {"status":"ok"}


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(problems.router)