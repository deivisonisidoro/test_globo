from datetime import datetime

import pytest

from src.domain.entities.video import VideoEntity
from src.infrastructure.database.models.video import VideoModel
from src.infrastructure.mappers.video import VideoMapper


@pytest.mark.unit
class TestVideoMapper:
    def test_to_entity(self):
        """Test the conversion from VideoModel to VideoEntity."""
        video_model = VideoModel(
            id="123e4567-e89b-12d3-a456-426614174000",
            url="https://example.com/video",
            created_at=datetime(2023, 1, 1),
            updated_at=datetime(2023, 1, 2),
        )

        video_entity = VideoMapper.to_entity(video_model)

        assert isinstance(video_entity, VideoEntity)
        assert video_entity.id == video_model.id
        assert video_entity.url == video_model.url
        assert video_entity.created_at == video_model.created_at
        assert video_entity.updated_at == video_model.updated_at

    def test_to_model(self):
        """Test the conversion from VideoEntity to VideoModel."""

        video_entity = VideoEntity(
            id="123e4567-e89b-12d3-a456-426614174000",
            url="https://example.com/video",
            created_at=datetime(2023, 1, 1),
            updated_at=datetime(2023, 1, 2),
        )

        video_model = VideoMapper.to_model(video_entity)

        assert isinstance(video_model, VideoModel)
        assert video_model.id == video_entity.id
        assert video_model.url == video_entity.url
        assert video_model.created_at == video_entity.created_at
        assert video_model.updated_at == video_entity.updated_at
