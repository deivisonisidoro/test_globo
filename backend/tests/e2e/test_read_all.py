from fastapi import status
from fastapi.testclient import TestClient
import pytest
from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.enums.success_messages import SuccessMessagesEnum
from src.presentation.schemas.create_video import CreateVideoSchema


@pytest.mark.e2e
class TestReadAllVideos:
    """
    End-to-end tests for reading all videos via the API.

    This class contains test cases to verify the behavior of the
    video retrieval endpoint.
    """

    def test_read_all_videos_success(self, client: TestClient):
        """
        Test the successful retrieval of all videos.

        This test simulates the scenario where videos are present in the database,
        and the API returns their 'id' and 'url' fields.

        Args:
            client (TestClient): The FastAPI test client for sending requests.
        """
        video_data_1 = CreateVideoSchema(url="https://www.example.com/video1")
        video_data_2 = CreateVideoSchema(url="https://www.example.com/video2")
        client.post("/api/videos/", json=video_data_1.model_dump())
        client.post("/api/videos/", json=video_data_2.model_dump())

        response = client.get("/api/videos/")
        assert response.status_code == status.HTTP_200_OK
        response_json = response.json()

        assert (
            response_json["message"]
            == SuccessMessagesEnum.VIDEOS_LISTED_SUCCESS.value
        )
        assert len(response_json["data"]) == 2
        assert "id" in response_json["data"][0]
        assert "url" in response_json["data"][0]

    def test_read_all_videos_empty(self, client: TestClient):
        """
        Test the retrieval of an empty list of videos.

        Args:
            client (TestClient): The FastAPI test client for sending requests.
        """
        response = client.get("/api/videos/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        response_json = response.json()

        assert (
            response_json["detail"] == ErrorMessagesEnum.NO_VIDEOS_FOUND.value
        )
