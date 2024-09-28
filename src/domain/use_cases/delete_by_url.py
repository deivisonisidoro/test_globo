from abc import ABC, abstractmethod

from src.domain.dtos.video_response import VideoResponseDTO


class AbstractDeleteVideoByUrlUseCase(ABC):
    """Abstract base class for deleting a video by URL."""

    @abstractmethod
    def execute(self, url: str) -> VideoResponseDTO:
        """Executes the use case to delete a video by its URL.

        Args:
            url (str): The URL of the video to delete.

        Returns:
            VideoResponseDTO: The DTO containing the status code and message.

        Raises:
            Exception: If an error occurs during deletion.
        """
        pass
