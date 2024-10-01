from abc import ABC, abstractmethod

from src.domain.dtos.video_response import VideoResponseDTO


class AbstractDeleteVideoUseCase(ABC):
    """Abstract base class for deleting a video by URL."""

    @abstractmethod
    def execute(self, id: str) -> VideoResponseDTO:
        """Executes the use case to delete a video by its ID.

        Args:
            id (str): The ID of the video to delete.

        Returns:
            (str): A success message.

        Raises:
            Exception: If an error occurs during deletion.
        """
        pass
