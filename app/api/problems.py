from fastapi import APIRouter, Depends


router = APIRouter(
    prefix="/problems",
    tags=["problems"]
)


@router.get("")
async def all_problems():
    return{"problems":"all"}
