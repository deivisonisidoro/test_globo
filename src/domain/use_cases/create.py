from abc import ABC, abstractmethod

from src.domain.dtos.video_response import VideoResponseDTO
from src.domain.repositories.videos import AbstractVideoRepository


class AbstractCreateVideoUseCase(ABC):
    """Abstract use case for video-related operations.

    This class defines the blueprint for handling video-related actions,
    such as creating a new video and checking for duplicates.
    """

    def __init__(self, video_repository: AbstractVideoRepository):
        """Initializes the abstract VideoUseCase.

        Args:
            video_repository (AbstractVideoRepository): The repository to store video entities.
        """
        self.video_repository = video_repository

    @abstractmethod
    def execute(self, url: str) -> VideoResponseDTO:
        """Abstract method for executing the video operation use case.

        Args:
            url (str): The URL of the video to create.

        Returns:
            VideoResponseDTO: The DTO containing the status code and created video entity.

        Raises:
            InvalidUrlError: If the URL is invalid or a video with the same URL already exists.
        """
        pass
