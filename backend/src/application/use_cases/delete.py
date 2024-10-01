from src.domain.dtos.video_response import VideoResponseDTO
from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.enums.success_messages import SuccessMessagesEnum
from src.domain.exceptions.validation_error.video_not_found_error import (
    VideoNotFoundError,
)
from src.domain.repositories.videos import AbstractVideoRepository
from src.domain.use_cases.delete import AbstractDeleteVideoUseCase


class DeleteVideoUseCase(AbstractDeleteVideoUseCase):
    """Concrete use case for deleting a video by URL."""

    def __init__(self, video_repository: AbstractVideoRepository):
        """Initializes the DeleteVideoUseCase.

        Args:
            video_repository (AbstractVideoRepository): The repository to delete video entities.
        """
        self.video_repository = video_repository

    def execute(self, id: str) -> str:
        """Deletes a video by its URL.

        Args:
            id (str): The ID of the video to delete.

        Returns:
            VideoResponseDTO: The DTO containing the status code and message.

        Raises:
            VideoNotFoundError: If no video with the given URL exists.
        """
        video = self.video_repository.find_by_id(id)

        if not video:
            raise VideoNotFoundError(
                message=ErrorMessagesEnum.NO_VIDEOS_FOUND.value,
                name="VideoNotFoundError",
            )

        self.video_repository.delete(video)

        return SuccessMessagesEnum.VIDEO_DELETED_SUCCESS.value
