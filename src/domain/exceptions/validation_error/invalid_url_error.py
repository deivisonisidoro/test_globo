from src.domain.exceptions.validation_error.video_validation_error import (
    VideoValidationError,
)


class InvalidUrlError(VideoValidationError):
    """Exception raised for invalid video URLs.

    This exception is used to indicate that a provided URL does not
    meet the required format or validation criteria for a video.
    It is a subclass of VideoValidationError, specifically for URL-related
    validation issues.

    Attributes:
        message (str): A description of the error.
        name (str): The name of the exception type.
    """

    pass
