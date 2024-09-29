from fastapi import APIRouter, Depends, status
from pytest import Session

from src.application.use_cases.create import CreateVideoUseCase
from src.infrastructure.database.connection import get_db
from src.infrastructure.repositories.video import VideoRepository
from src.presentation.schemas.create_video import CreateVideoSchema
from src.presentation.schemas.success_message import SuccessMessageSchema

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new video",
    description="Create a new video with the provided data in the request body.",
    response_model=SuccessMessageSchema,
)
def create_video(video: CreateVideoSchema, db: Session = Depends(get_db)):
    """
    Creates a new video entry in the database.

    This endpoint allows the user to create a new video by providing
    the necessary details in the request body. The video information
    will be stored in the database, and a success message is returned.

    Args:
        video (CreateVideoSchema): The schema that contains the video data, including title, description, duration, and url.
        db (Session, optional): The database session dependency, provided by FastAPI's Depends.

    Returns:
        dict: A response containing a success message and the created video's URL in the data field.

    Example:
        Response:
        {
            "message": "Video created successfully",
            "data": {
                "url": "https://www.example.com/video"
            }
        }
    """
    repository = VideoRepository(session=db)
    use_case = CreateVideoUseCase(video_repository=repository)
    created_video = use_case.execute(video.url)
    response_data = {
        "message": "Video created successfully",
        "data": {"url": created_video.url},
    }
    return response_data
