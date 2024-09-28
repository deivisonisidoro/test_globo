class VideoValidationError(Exception):
    """Custom exception for video validation errors.

    This exception is raised when there are validation issues related to
    video entities, such as invalid URLs or other constraints.

    Attributes:
        message (str): A description of the error.
        name (str): The name of the exception type.
    """

    def __init__(
        self,
        message: str = "A video validation error occurred.",
        name: str = "VideoValidationError",
    ) -> None:
        """Initializes the VideoValidationError with an optional message and name.

        Args:
            message (str): A description of the error. Defaults to
                "A video validation error occurred."
            name (str): The name of the exception type. Defaults to
                "VideoValidationError".
        """
        self.message = message
        self.name = name
        super().__init__(self.message)

    def __str__(self) -> str:
        """Returns a string representation of the VideoValidationError.

        Returns:
            str: A string that represents the error, including its name
                and message.
        """
        return f"{self.name}: {self.message}"


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


class DuplicateUrlError(VideoValidationError):
    """Exception raised for duplicate video URLs.

    This exception is used to indicate that a provided URL already exists
    in the system, and thus cannot be used to create a new video.
    It is a subclass of VideoValidationError, specifically for duplicate
    URL-related issues.
    """

    pass
