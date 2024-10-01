import pytest
from fastapi import status
from fastapi.testclient import TestClient

from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.enums.success_messages import SuccessMessagesEnum
from src.presentation.schemas.create_video import CreateVideoSchema


@pytest.mark.e2e
class TestCreateVideo:
    """
    End-to-end tests for the video creation feature in the FastAPI application.

    This class contains test cases to verify the behavior of the
    video creation endpoint. It ensures that the API correctly
    handles the creation of a new video and returns the expected
    response when provided with valid data.

    Attributes:
        client (TestClient): A FastAPI test client used for making
                             requests to the API.
    """

    def test_create_video(self, client: TestClient):
        """
        Test the creation of a video via the API.

        This test sends a POST request to the /api/videos/ endpoint
        with a valid video payload. It checks that the response status
        code is 201 (Created) and verifies that the response message
        and data are as expected.

        Args:
            client (TestClient): The FastAPI test client for sending
                                 requests.
        """
        video_data = CreateVideoSchema(url="https://www.example.com/video")

        response = client.post("api/videos/", json=video_data.model_dump())

        assert response.status_code == status.HTTP_201_CREATED

        response_data = response.json()
        assert (
            response_data["message"]
            == SuccessMessagesEnum.VIDEO_CREATED_SUCCESS.value
        )
        assert response_data["data"]["url"] == video_data.url

    def test_create_duplicate_video(self, client: TestClient):
        """
        Test the creation of a duplicate video via the API.

        This test attempts to create a video with a URL that
        already exists in the database. It checks that a
        DuplicateUrlError is raised.

        Args:
            client (TestClient): The FastAPI test client for sending
                                requests.
        """
        video_data = CreateVideoSchema(url="https://www.example.com/video")

        response = client.post("api/videos/", json=video_data.model_dump())

        assert response.status_code == status.HTTP_201_CREATED

        duplicate_response = client.post(
            "api/videos/", json=video_data.model_dump()
        )

        assert duplicate_response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            duplicate_response.json()["detail"]
            == ErrorMessagesEnum.DUPLICATE_URL.value
        )

    def test_create_video_invalid_url(self, client: TestClient):
        """
        Test the creation of a video with an invalid URL via the API.

        This test attempts to create a video with a malformed URL. It
        checks that the API returns an error indicating that the URL
        is invalid.

        Args:
            client (TestClient): The FastAPI test client for sending
                                 requests.
        """
        video_data = CreateVideoSchema(url="invalid-url")

        response = client.post("/api/videos/", json=video_data.model_dump())

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert response.json()["detail"] == ErrorMessagesEnum.INVALID_URL.value

    def test_create_video_without_url(self, client: TestClient):
        """
        Test the creation of a video without a URL via the API.

        This test attempts to create a video with a missing URL. It
        checks that the API returns an error indicating that the URL
        is required.

        Args:
            client (TestClient): The FastAPI test client for sending
                                 requests.
        """

        response = client.post("/api/videos/", json={})

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
