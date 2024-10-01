from src.domain.entities.video import VideoEntity
from src.infrastructure.database.models import VideoModel


class VideoMapper:
    """
    A mapper class that converts between VideoEntity (domain) and VideoModel (infrastructure).
    """

    @staticmethod
    def to_entity(video_model: VideoModel) -> VideoEntity:
        """
        Converts a VideoModel instance into a VideoEntity.

        Args:
            video_model (VideoModel): The database model of the video.

        Returns:
            VideoEntity: The corresponding domain entity.
        """
        return VideoEntity(
            id=video_model.id,
            url=video_model.url,
            created_at=video_model.created_at,
            updated_at=video_model.updated_at,
        )

    @staticmethod
    def to_model(video_entity: VideoEntity) -> VideoModel:
        """
        Converts a VideoEntity instance into a VideoModel.

        Args:
            video_entity (VideoEntity): The domain entity of the video.

        Returns:
            VideoModel: The corresponding database model.
        """
        return VideoModel(
            id=video_entity.id,
            url=video_entity.url,
            created_at=video_entity.created_at,
            updated_at=video_entity.updated_at,
        )
