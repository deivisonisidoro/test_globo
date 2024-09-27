import uuid
from datetime import datetime

import pytest

from src.domain.entities.video import VideoEntity
from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.factories.video import VideoFactory


class TestVideoFactory:
    """
    A test suite for the VideoFactory class using pytest.

    This class tests various scenarios for creating VideoEntity instances,
    including handling of default values, validation of URLs, and generation of UUIDs.
    """

    def test_create_video_with_all_fields(self):
        """
        Test creating a VideoEntity with all fields provided (id, url, created_at, updated_at).
        """
        url = "https://example.com/video"
        video_id = uuid.uuid4()
        created_at = datetime(2023, 9, 25, 12, 0)
        updated_at = datetime(2023, 9, 25, 13, 0)

        video = VideoFactory.create(
            url=url, id=video_id, created_at=created_at, updated_at=updated_at
        )

        assert isinstance(video, VideoEntity)
        assert video.url == url
        assert video.id == video_id
        assert video.created_at == created_at
        assert video.updated_at == updated_at

    def test_create_video_with_defaults(self):
        """
        Test creating a VideoEntity with only the URL provided.
        """
        url = "https://example.com/video"

        video = VideoFactory.create(url=url)

        assert isinstance(video, VideoEntity)
        assert video.url == url
        assert isinstance(video.id, uuid.UUID)
        assert isinstance(video.created_at, datetime)
        assert video.updated_at is None

    def test_create_video_with_defaults_method(self):
        """
        Test creating a VideoEntity using the create_with_defaults method.
        """

        video = VideoFactory.create_with_defaults()

        assert isinstance(video, VideoEntity)
        assert video.url == "https://example.com/default-video"
        assert isinstance(video.id, uuid.UUID)
        assert isinstance(video.created_at, datetime)
        assert video.updated_at is None

    def test_invalid_url_raises_error(self):
        """
        Test that providing an invalid URL raises a ValueError.
        """
        invalid_url = "ftp://invalid-url.com"

        with pytest.raises(ValueError) as exc_info:
            VideoFactory.create(url=invalid_url)

        assert str(exc_info.value) == ErrorMessagesEnum.INVALID_URL.value

    def test_create_video_with_no_id_generates_uuid(self):
        """
        Test that the factory generates a UUID if none is provided.
        """
        url = "https://example.com/video"

        video = VideoFactory.create(url=url)

        assert isinstance(video.id, uuid.UUID)

    def test_create_video_with_no_created_at_generates_current_datetime(self):
        """
        Test that the factory sets the created_at field to the current time if none is provided.

        """
        url = "https://example.com/video"

        video = VideoFactory.create(url=url)

        assert isinstance(video.created_at, datetime)
        assert video.created_at <= datetime.now()

    def test_create_video_with_updated_at(self):
        """
        Test that providing an updated_at value sets it correctly in the VideoEntity.
        """
        url = "https://example.com/video"
        updated_at = datetime(2023, 9, 25, 13, 0)

        video = VideoFactory.create(url=url, updated_at=updated_at)

        assert video.updated_at == updated_at
