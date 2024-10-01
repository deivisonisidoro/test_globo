from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.video import VideoEntity


class AbstractReadAllVideosUseCase(ABC):
    """Abstract use case for retrieving all videos.

    This class defines the blueprint for handling the retrieval of all video entities from the repository.
    """

    @abstractmethod
    def execute(self) -> List[VideoEntity]:
        """Abstract method for retrieving all videos.

        This method should be implemented by subclasses to return a list of videos.

        Returns:
            (VideoNotFoundError): If no videos are found in the repository.
        """
        pass
