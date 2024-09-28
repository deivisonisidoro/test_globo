import pytest
from sqlalchemy.orm import Session

from src.domain.factories.video import VideoFactory
from src.infrastructure.repositories.video import VideoRepository


@pytest.fixture
def video_repository(in_memory_session: Session) -> VideoRepository:
    """Fixture for initializing a VideoRepository with an in-memory database session.

    Args:
        in_memory_session (Session): An SQLAlchemy session configured for in-memory operations.

    Returns:
        (VideoRepository): An instance of VideoRepository for managing video data in the in-memory database.
    """
    return VideoRepository(in_memory_session)


@pytest.mark.integration
class TestVideoRepository:
    """
    Integration tests for the VideoRepository.
    """

    def test_create_video(self, video_repository):
        """
        Tests the creation of a video in the database.
        """
        video = VideoFactory.create(url="https://example.com/video1")
        created_video = video_repository.create(video)

        assert created_video.id is not None
        assert created_video.url == "https://example.com/video1"
        assert created_video.created_at is not None

    def test_find_by_url(self, video_repository):
        """
        Tests the retrieval of a video by URL in the database.
        """
        video = VideoFactory.create(url="https://example.com/video2")
        video_repository.create(video)

        found_video = video_repository.find_by_url(
            "https://example.com/video2"
        )
        assert found_video is not None
        assert found_video.url == "https://example.com/video2"

    def test_find_all_videos(self, video_repository):
        """
        Tests the retrieval of all videos in the database.
        """
        video_repository.create(
            VideoFactory.create(url="https://example.com/video3")
        )
        video_repository.create(
            VideoFactory.create(url="https://example.com/video4")
        )

        videos = video_repository.find_all()

        assert len(videos) == 2

    def test_delete_video(self, video_repository):
        """
        Tests the deletion of a video from the database.
        """
        video = VideoFactory.create(url="https://example.com/video5")
        created_video = video_repository.create(video)

        video_repository.delete(created_video)
        deleted_video = video_repository.find_by_url(
            "https://example.com/video5"
        )

        assert deleted_video is None
