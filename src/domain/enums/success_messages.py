from enum import Enum


class SuccessMessagesEnum(Enum):
    """
    Enum for success messages used in the application.

    This enum contains standardized messages for success responses,
    such as when a video is created or deleted successfully. Using
    enums for success messages helps ensure consistency across the
    application.

    Attributes:
        VIDEO_CREATED_SUCCESS (str): Message returned when a video is successfully created.
        VIDEO_DELETED_SUCCESS (str): Message returned when a video is successfully deleted.
    """

    VIDEO_CREATED_SUCCESS = "Video created successfully"
    VIDEO_DELETED_SUCCESS = "Video deleted successfully"
