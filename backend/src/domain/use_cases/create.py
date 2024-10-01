from abc import ABC, abstractmethod

from src.domain.entities.video import VideoEntity


class AbstractCreateVideoUseCase(ABC):
    """Abstract use case for video-related operations.

    This class defines the blueprint for handling video-related actions,
    such as creating a new video and checking for duplicates.
    """

    @abstractmethod
    def execute(self, url: str) -> VideoEntity:
        """Abstract method for executing the video operation use case.

        Args:
            url (str): The URL of the video to create.

        Returns:
            VideoEntity: A video entity instance

        Raises:
            InvalidUrlError: If the URL is invalid or a video with the same URL already exists.
        """
        pass
