from typing import List
from src.domain.entities.video import VideoEntity
from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.exceptions.validation_error import VideoNotFoundError
from src.domain.repositories.videos import AbstractVideoRepository
from src.domain.use_cases.read_all import AbstractReadAllVideosUseCase


class ReadAllVideosUseCase(AbstractReadAllVideosUseCase):
    """Concrete use case for retrieving all videos.

    This class implements the logic for fetching all video entities from the repository.
    """

    def __init__(self, video_repository: AbstractVideoRepository):
        """Initializes the abstract ReadAllVideosUseCase.

        Args:
            video_repository (AbstractVideoRepository): The repository to retrieve video entities.
        """
        self.video_repository = video_repository

    def execute(self) -> List[VideoEntity]:
        """Fetches all videos from the repository.

        Returns:
            (VideoResponseDTO): The DTO containing the status code and list of video entities.

        Raises:
            VideoNotFoundError: If no videos are found in the repository.
        """
        videos = self.video_repository.find_all()

        if not videos:
            raise VideoNotFoundError(
                message=ErrorMessagesEnum.NO_VIDEOS_FOUND.value,
                name="VideoNotFoundError",
            )

        return videos
