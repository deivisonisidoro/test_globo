from pydantic import BaseModel, Field


class CreateVideoSchema(BaseModel):
    """
    Schema for creating a new video.

    This schema defines the structure of the request body required to create
    a new video. It expects a URL of the video that will be stored in the database.

    Attributes:
        url (str): The URL of the video that is being created. Must be a valid string.
    """

    url: str = Field(..., description="Video URL")

    class Config:
        schema_extra = {"example": {"url": "https://www.example.com/video"}}
