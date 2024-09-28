from enum import Enum


class ErrorMessagesEnum(Enum):
    """
    Enum for error messages used in the validation of VideoEntity attributes.

    Attributes:
        INVALID_URL (str): Error message when the URL is invalid.
            The URL must start with 'http' or 'https'.
        DUPLICATE_URL (str): Error message when a video with the same URL
            already exists in the system.
        NO_VIDEOS_FOUND (str): Error message when no videos are found in the system.
    """

    INVALID_URL = "Invalid URL. The URL must start with 'http' or 'https'."
    DUPLICATE_URL = "A video with the same URL already exists."
    NO_VIDEOS_FOUND = "No videos were found."
