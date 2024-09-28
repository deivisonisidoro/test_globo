from src.domain.dtos.video_response import VideoResponseDTO
from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.exceptions.validation_error.video_not_found_error import (
    VideoNotFoundError,
)
from src.domain.repositories.videos import AbstractVideoRepository
from src.domain.use_cases.delete_by_url import AbstractDeleteVideoByUrlUseCase


class DeleteVideoByUrlUseCase(AbstractDeleteVideoByUrlUseCase):
    """Concrete use case for deleting a video by URL."""

    def __init__(self, video_repository: AbstractVideoRepository):
        """Initializes the DeleteVideoByUrlUseCase.

        Args:
            video_repository (AbstractVideoRepository): The repository to delete video entities.
        """
        self.video_repository = video_repository

    def execute(self, url: str) -> VideoResponseDTO:
        """Deletes a video by its URL.

        Args:
            url (str): The URL of the video to delete.

        Returns:
            VideoResponseDTO: The DTO containing the status code and message.

        Raises:
            VideoNotFoundError: If no video with the given URL exists.
        """
        video = self.video_repository.find_by_url(url)

        if not video:
            raise VideoNotFoundError(
                message=ErrorMessagesEnum.NO_VIDEOS_FOUND.value,
                name="VideoNotFoundError",
            )

        self.video_repository.delete(video)

        return VideoResponseDTO(
            status_code=204, data={"message": "Video deleted successfully."}
        )
