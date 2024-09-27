from datetime import datetime
from typing import Optional
import uuid
import re


class VideoEntity:
    """
    A class representing a video entity.

    Attributes:
        id (Optional[uuid.UUID]): Unique identifier for the video. Defaults to None, will generate a UUID if not provided.
        url (str): URL of the video. Required field.
        created_at (Optional[datetime]): Date and time when the video was created. Defaults to the current time.
        updated_at (Optional[datetime]): Date and time when the video was last updated. Defaults to None.
    """

    URL_REGEX = re.compile(r"^(http|https)://")

    def __init__(
        self,
        url: str,
        id: Optional[uuid.UUID] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        """
        Initializes a new instance of the VideoEntity class.

        Args:
            url (str): The URL of the video. Must start with http or https.
            id (Optional[uuid.UUID]): Unique identifier for the video. If None, a UUID will be generated.
            created_at (Optional[datetime]): The creation time of the video. Defaults to the current time.
            updated_at (Optional[datetime]): The last updated time of the video. Defaults to None.

        Raises:
            ValueError: If the provided URL is invalid.
        """
        self._id = id or uuid.uuid4()
        self.url = url
        self._created_at = created_at or datetime.now()
        self._updated_at = updated_at

    @property
    def id(self) -> uuid.UUID:
        """Gets the unique identifier of the video."""
        return self._id

    @id.setter
    def id(self, value: Optional[uuid.UUID]) -> None:
        """Sets the unique identifier of the video."""
        self._id = value or uuid.uuid4()

    @property
    def url(self) -> str:
        """Gets the URL of the video."""
        return self._url

    @url.setter
    def url(self, value: str) -> None:
        """
        Sets the URL of the video with validation.

        Args:
            value (str): The new URL of the video. Must be a valid URL starting with http or https.

        Raises:
            ValueError: If the URL is invalid.
        """
        if not self.URL_REGEX.match(value):
            raise ValueError("Invalid URL. The URL must start with 'http' or 'https'.")
        self._url = value

    @property
    def created_at(self) -> datetime:
        """Gets the creation timestamp of the video."""
        return self._created_at

    @created_at.setter
    def created_at(self, value: Optional[datetime]) -> None:
        """
        Sets the creation timestamp of the video.

        Args:
            value (Optional[datetime]): The new creation date and time. Defaults to the current time.
        """
        self._created_at = value or datetime.now()

    @property
    def updated_at(self) -> Optional[datetime]:
        """Gets the last updated timestamp of the video."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value: datetime):
        """Sets the updated_at timestamp.

        Args:
            value (datetime): The new updated timestamp.
        """
        if value is not None:
            self._updated_at = value
        else:
            self._updated_at = datetime.now()

    def __repr__(self) -> str:
        """
        Returns a string representation of the VideoEntity instance.

        Returns:
            str: A string that represents the video entity, including its id, URL, and timestamps.
        """
        return (
            f"VideoEntity(id={self.id}, url='{self.url}', "
            f"created_at='{self.created_at}', updated_at='{self.updated_at}')"
        )
