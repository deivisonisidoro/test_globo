from dataclasses import dataclass

from src.domain.entities.video import VideoEntity


@dataclass
class VideoResponseDTO:
    """Data Transfer Object for Video response.

    This class represents the response structure returned by video-related operations,
    containing the status code and video data.

    Attributes:
        status_code (int): The HTTP status code.
        data (VideoEntity): The created or retrieved video entity.
    """

    status_code: int
    data: VideoEntity

    def __init__(self, status_code: int, data: VideoEntity):
        """Initializes the VideoResponseDTO.

        Args:
            status_code (int): The HTTP status code.
            data (VideoEntity): The video entity associated with the response.
        """
        self.status_code = status_code
        self.data = data
