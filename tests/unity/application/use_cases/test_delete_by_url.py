from unittest.mock import MagicMock

import pytest

from src.application.use_cases.delete_by_url import DeleteVideoByUrlUseCase
from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.exceptions.validation_error import VideoNotFoundError
from src.domain.factories.video import VideoFactory
from src.domain.repositories.videos import AbstractVideoRepository


class TestDeleteVideoByUrlUseCase:
    def setup_method(self):
        """Setup a new instance of DeleteVideoByUrlUseCase for each test."""
        self.video_repository = MagicMock(spec=AbstractVideoRepository)
        self.delete_video_use_case = DeleteVideoByUrlUseCase(
            self.video_repository
        )

    def test_delete_video_success(self):
        """Test successful deletion of a video."""
        video_url = "http://example.com/video"
        video_entity = VideoFactory.create(url=video_url)

        self.video_repository.find_by_url.return_value = video_entity
        self.video_repository.delete.return_value = None

        self.delete_video_use_case.execute(video_url)

        self.video_repository.find_by_url.assert_called_once_with(video_url)
        self.video_repository.delete.assert_called_once_with(video_entity)

    def test_delete_NO_VIDEOS_FOUND(self):
        """Test deletion when the video is not found."""
        video_url = "http://example.com/nonexistent"

        self.video_repository.find_by_url.return_value = None

        with pytest.raises(VideoNotFoundError) as excinfo:
            self.delete_video_use_case.execute(video_url)

        assert excinfo.value.message == ErrorMessagesEnum.NO_VIDEOS_FOUND.value
        assert excinfo.value.name == "VideoNotFoundError"
