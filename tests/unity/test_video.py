import uuid
from datetime import datetime

import pytest

from src.domain.entities.video import VideoEntity


class TestVideoEntity:
    """Test suite for the VideoEntity class."""

    def test_video_entity_creation(self):
        """Test the creation of a VideoEntity with a valid URL."""
        url = "https://example.com"
        video = VideoEntity(url=url)

        assert video.url == url
        assert isinstance(video.id, uuid.UUID)
        assert isinstance(video.created_at, datetime)
        assert video.updated_at is None

    def test_video_entity_uuid_generation(self):
        """Test that a UUID is generated when no id is provided."""
        video = VideoEntity(url="https://example.com")

        assert isinstance(video.id, uuid.UUID)

    def test_video_entity_url_validation(self):
        """Test that an invalid URL raises a ValueError."""
        with pytest.raises(ValueError):
            VideoEntity(url="invalid_url")

    def test_video_entity_manual_id(self):
        """Test setting a custom UUID."""
        custom_id = uuid.uuid4()
        video = VideoEntity(url="https://example.com", id=custom_id)

        assert video.id == custom_id

    def test_created_at_field(self):
        """Test that the created_at field is automatically set."""
        video = VideoEntity(url="https://example.com")

        assert isinstance(video.created_at, datetime)
        assert video.created_at <= datetime.now()

    def test_updated_at_on_url_change(self):
        """Test that updated_at is updated when the URL is modified."""
        video = VideoEntity(url="https://example.com")
        assert video.updated_at is None

    def test_updated_at_does_not_change_on_creation(self):
        """Test that updated_at remains None if nothing changes."""
        video = VideoEntity(url="https://example.com")

        assert video.updated_at is None

    def test_setting_created_at(self):
        """Test setting the created_at field manually."""
        custom_time = datetime(2022, 1, 1)
        video = VideoEntity(url="https://example.com", created_at=custom_time)

        assert video.created_at == custom_time

    def test_setting_updated_at_manually(self):
        """Test manually setting the updated_at field."""
        custom_time = datetime(2023, 1, 1)
        video = VideoEntity(url="https://example.com", updated_at=custom_time)

        assert video.updated_at == custom_time
