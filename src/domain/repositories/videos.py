from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.video import VideoEntity


class AbstractVideoRepository(ABC):
    """Abstract base class for video repositories.

    This class defines the methods that any concrete video repository must implement.
    """

    @abstractmethod
    def create(self, video: VideoEntity) -> VideoEntity:
        """Creates a new video in the repository.

        Args:
            video (VideoEntity): The video entity to create.

        Returns:
            VideoEntity: The created video entity.
        """
        pass

    @abstractmethod
    def find_by_url(self, url: str) -> Optional[VideoEntity]:
        """Finds a video by URL.

        Args:
            url (str): The URL of the video to find.

        Returns:
            Optional[VideoEntity]: The found video entity or None if not found.
        """
        pass

    @abstractmethod
    def find_all(self) -> List[VideoEntity]:
        """Finds all videos in the repository.

        Returns:
            List[VideoEntity]: A list of all video entities in the repository.
        """
        pass
