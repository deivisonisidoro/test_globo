from unittest.mock import Mock

import pytest

from src.application.use_cases.read_all import ReadAllVideosUseCase
from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.exceptions.validation_error.video_not_found_error import (
    VideoNotFoundError,
)
from src.domain.factories.video import VideoFactory
from src.domain.repositories.videos import AbstractVideoRepository


@pytest.mark.unit
class TestReadAllVideosUseCase:
    """Test suite for ReadAllVideosUseCase."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up a mock video repository and use case before each test."""
        self.mock_video_repository = Mock(spec=AbstractVideoRepository)
        self.use_case = ReadAllVideosUseCase(
            video_repository=self.mock_video_repository
        )

    def test_read_all_videos_success(self):
        """Test case when videos are found in the repository."""
        video1 = VideoFactory.create(url="http://example.com/video1")
        video2 = VideoFactory.create(url="http://example.com/video2")
        self.mock_video_repository.find_all.return_value = [video1, video2]

        response = self.use_case.execute()

        assert len(response) == 2
        assert response[0].url == "http://example.com/video1"
        assert response[1].url == "http://example.com/video2"
        self.mock_video_repository.find_all.assert_called_once()

    def test_read_all_videos_not_found(self):
        """Test case when no videos are found in the repository."""
        self.mock_video_repository.find_all.return_value = []

        with pytest.raises(VideoNotFoundError) as exc_info:
            self.use_case.execute()

        assert (
            exc_info.value.message == ErrorMessagesEnum.NO_VIDEOS_FOUND.value
        )
        assert exc_info.value.name == "VideoNotFoundError"
        self.mock_video_repository.find_all.assert_called_once()
