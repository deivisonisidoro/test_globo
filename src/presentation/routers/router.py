from fastapi import APIRouter

from src.presentation.routers import video

router = APIRouter()

router.include_router(video.router, prefix="/videos", tags=["Video"])
