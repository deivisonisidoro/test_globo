from src.domain.exceptions.validation_error.video_validation_error import (
    VideoValidationError,
)


class DuplicateUrlError(VideoValidationError):
    """Exception raised for duplicate video URLs.

    This exception is used to indicate that a provided URL already exists
    in the system, and thus cannot be used to create a new video.
    It is a subclass of VideoValidationError, specifically for duplicate
    URL-related issues.
    """

    pass
