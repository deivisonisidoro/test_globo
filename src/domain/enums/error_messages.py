from enum import Enum


class ErrorMessagesEnum(Enum):
    """
    Enum for error messages used in the validation of VideoEntity attributes.

    Attributes:
        INVALID_URL (str): Error message when the URL is invalid.
            The URL must start with 'http' or 'https'.
        DUPLICATE_URL (str): Error message when a video with the same URL
            already exists in the system.
    """

    INVALID_URL = "URL inválida. A URL deve começar com 'http' ou 'https'."
    DUPLICATE_URL = "A video with the same URL already exists."
