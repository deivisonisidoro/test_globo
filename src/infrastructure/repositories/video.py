from typing import List, Optional

from sqlalchemy.orm import Session

from src.domain.entities.video import VideoEntity
from src.domain.repositories.videos import AbstractVideoRepository
from src.infrastructure.database.models.video import VideoModel
from src.infrastructure.mappers.video import VideoMapper


class VideoRepository(AbstractVideoRepository):
    """
    Concrete implementation of the AbstractVideoRepository using SQLAlchemy.

    This repository is responsible for managing video data in the database.
    """

    def __init__(self, session: Session):
        """
        Initializes the repository with a SQLAlchemy session.

        Args:
            session (Session): The SQLAlchemy session used for database interactions.
        """
        self.session = session

    def create(self, video: VideoEntity) -> VideoEntity:
        """
        Creates a new video in the database.

        Args:
            video (VideoEntity): The video entity to create.

        Returns:
            VideoEntity: The created video entity.
        """
        video_model = VideoMapper.to_model(video)
        self.session.add(video_model)
        self.session.commit()
        self.session.refresh(
            video_model
        )  # Refresh to get the updated fields like 'id'
        return VideoMapper.to_entity(video_model)

    def find_by_url(self, url: str) -> Optional[VideoEntity]:
        """
        Finds a video by its URL in the database.

        Args:
            url (str): The URL of the video to find.

        Returns:
            Optional[VideoEntity]: The found video entity or None if not found.
        """
        video_model = self.session.query(VideoModel).filter_by(url=url).first()
        if video_model:
            return VideoMapper.to_entity(video_model)
        return None

    def find_all(self) -> List[VideoEntity]:
        """
        Retrieves all video entities from the database.

        Returns:
            List[VideoEntity]: A list of all video entities.
        """
        video_models = self.session.query(VideoModel).all()
        return [
            VideoMapper.to_entity(video_model) for video_model in video_models
        ]

    def delete(self, video: VideoEntity) -> None:
        """
        Deletes a video from the database.

        Args:
            video (VideoEntity): The video entity to delete.
        """
        video_model = (
            self.session.query(VideoModel).filter_by(id=video.id).first()
        )
        if video_model:
            self.session.delete(video_model)
            self.session.commit()
