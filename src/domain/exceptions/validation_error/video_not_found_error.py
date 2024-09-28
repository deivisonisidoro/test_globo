from src.domain.exceptions.validation_error.video_validation_error import (
    VideoValidationError,
)


class VideoNotFoundError(VideoValidationError):
    """Exception raised when a video is not found.

    This exception is used to indicate that a video entity was not found
    in the system. It is a subclass of VideoValidationError, specifically
    for video-not-found issues.
    """

    pass
