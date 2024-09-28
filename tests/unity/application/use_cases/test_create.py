from unittest.mock import MagicMock

import pytest

from src.application.use_cases.create import CreateVideoUseCase
from src.domain.entities.video import VideoEntity
from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.exceptions.video_validation_error import DuplicateUrlError
from src.domain.factories.video import VideoFactory
from src.domain.repositories.videos import AbstractVideoRepository


class TestCreateVideoUseCase:
    """Test suite for CreateVideoUseCase."""

    def setup_method(self):
        """Setup method to initialize test objects."""
        self.video_repository = MagicMock(spec=AbstractVideoRepository)
        self.use_case = CreateVideoUseCase(self.video_repository)

    def test_execute_creates_video_successfully(self):
        """Test that a video is created successfully."""
        url = "https://example.com/video"
        expected_video = VideoFactory.create(url)

        self.video_repository.find_by_url.return_value = None
        self.video_repository.create.return_value = expected_video

        created_video = self.use_case.execute(url)

        self.video_repository.find_by_url.assert_called_once_with(url)
        self.video_repository.create.assert_called_once()
        assert created_video.data.url == expected_video.url

    def test_execute_raises_invalid_url_error_on_duplicate_url(self):
        """Test that an DuplicateUrlError is raised for duplicate URLs."""
        url = "https://example.com/video"
        existing_video = VideoEntity(url=url)

        self.video_repository.find_by_url.return_value = existing_video

        with pytest.raises(DuplicateUrlError) as exc_info:
            self.use_case.execute(url)

        assert (
            str(exc_info.value.message)
            == ErrorMessagesEnum.DUPLICATE_URL.value
        )
        self.video_repository.find_by_url.assert_called_once_with(url)
        self.video_repository.create.assert_not_called()
