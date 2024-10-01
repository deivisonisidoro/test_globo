from src.domain.entities.video import VideoEntity
from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.exceptions.validation_error import DuplicateUrlError
from src.domain.factories.video import VideoFactory
from src.domain.repositories.videos import AbstractVideoRepository
from src.domain.use_cases.create import AbstractCreateVideoUseCase


class CreateVideoUseCase(AbstractCreateVideoUseCase):
    """Use case for video-related operations.

    This class encapsulates the business logic for handling video-related actions,
    such as creating a new video and checking for duplicates.
    """

    def __init__(self, video_repository: AbstractVideoRepository):
        """Initializes the VideoUseCase.

        Args:
            video_repository (AbstractVideoRepository): The repository to store video entities.
        """
        self.video_repository = video_repository

    def execute(self, url: str) -> VideoEntity:
        """Executes the use case to handle video operations.

        This method verifies if a video with the same URL already exists before creating a new one.

        Args:
            url (str): The URL of the video to create.

        Returns:
            (VideoEntity): A instance of video entity

        Raises:
            (InvalidUrlError): If the URL is invalid or a video with the same URL already exists.
        """
        existing_video = self.video_repository.find_by_url(url)
        if existing_video:
            raise DuplicateUrlError(
                message=ErrorMessagesEnum.DUPLICATE_URL.value,
                name="DuplicateUrl",
            )

        new_video = VideoFactory.create(url)

        created_video = self.video_repository.create(new_video)

        return created_video
