# app/infrastructure/models/video_model.py
import re
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates

from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.exceptions.validation_error.invalid_url_error import (
    InvalidUrlError,
)
from src.infrastructure.database.connection import Base


class VideoModel(Base):
    """
    A SQLAlchemy model representing the 'videos' table in the database.

    Attributes:
        id (UUID): Unique identifier for each video. It is automatically generated using UUID.
        url (str): The URL of the video, which must start with "http" or "https".
        created_at (datetime): Timestamp representing when the video record was created. Defaults to the current UTC time.
        updated_at (datetime): Timestamp representing when the video record was last updated. This can be null if no update has occurred.

    Methods:
        validate_url(key, url):
            Validates that the URL follows the correct format (starting with "http" or "https").
            Raises InvalidUrlError if the URL does not match the expected pattern.
    """

    __tablename__ = "videos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)

    URL_REGEX = re.compile(r"^(http|https)://")

    @validates("url")
    def validate_url(self, key, url):
        """
        Validates the 'url' field to ensure it starts with "http" or "https".

        Args:
            key (str): The field name being validated (in this case, 'url').
            url (str): The URL string to validate.

        Returns:
            (str): The validated URL if it matches the required pattern.

        Raises:
            InvalidUrlError: If the URL does not match the required "http" or "https" format.
        """
        if not self.URL_REGEX.match(url):
            raise InvalidUrlError(
                message=ErrorMessagesEnum.INVALID_URL.value, name="InvalidUrl"
            )
        return url
