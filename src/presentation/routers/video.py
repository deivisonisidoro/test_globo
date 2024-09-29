from uuid import UUID

from fastapi import APIRouter, Depends, status
from pytest import Session

from src.application.use_cases.create import CreateVideoUseCase
from src.application.use_cases.delete import DeleteVideoUseCase
from src.domain.enums.success_messages import SuccessMessagesEnum
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
        "message": SuccessMessagesEnum.VIDEO_CREATED_SUCCESS.value,
        "data": {"id": created_video.id, "url": created_video.url},
    }
    return response_data


@router.delete(
    "/{video_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a video",
    description="Delete a video from the database by its ID.",
)
def delete_video(video_id: UUID, db: Session = Depends(get_db)):
    """
    Deletes a video entry from the database.

    This endpoint allows the user to delete a video by providing
    the unique video ID in the request path. If the video is
    successfully deleted, a 204 No Content response is returned.

    Args:
        video_id (str): The unique identifier of the video to be deleted.
        db (Session, optional): The database session dependency, provided by FastAPI's Depends.

    Returns:
        (str): A response with no content (204).
    """
    repository = VideoRepository(session=db)
    use_case = DeleteVideoUseCase(video_repository=repository)
    use_case.execute(id=video_id)

    return None
