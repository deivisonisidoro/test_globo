import uuid
from datetime import datetime
from typing import Optional

from src.domain.entities.video import VideoEntity


class VideoFactory:
    """
    A factory class for creating instances of VideoEntity.
    """

    @staticmethod
    def create(
        url: str,
        id: Optional[uuid.UUID] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> VideoEntity:
        """
        Creates and returns a new instance of VideoEntity with optional parameters for id, created_at, and updated_at.

        Args:
            url (str): The URL of the video. Must start with http or https.
            id (Optional[uuid.UUID]): Unique identifier for the video. If None, a UUID will be generated.
            created_at (Optional[datetime]): The creation time of the video. Defaults to the current time.
            updated_at (Optional[datetime]): The last updated time of the video. Defaults to None.

        Returns:
            VideoEntity: A new instance of VideoEntity.
        """
        return VideoEntity(
            url=url,
            id=id or uuid.uuid4(),
            created_at=created_at or datetime.now(),
            updated_at=updated_at,
        )

    @staticmethod
    def create_with_defaults() -> VideoEntity:
        """
        Creates and returns a new instance of VideoEntity with default values.

        Returns:
            VideoEntity: A new instance of VideoEntity with default URL and current timestamp.
        """
        default_url = "https://example.com/default-video"
        return VideoFactory.create(url=default_url)
