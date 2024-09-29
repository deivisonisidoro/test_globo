import pytest
from fastapi import status
from fastapi.testclient import TestClient

from src.application.use_cases.delete import DeleteVideoUseCase
from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.enums.success_messages import SuccessMessagesEnum


@pytest.mark.e2e
class TestDeleteVideo:
    """
    End-to-end tests for the video deletion feature in the FastAPI application.

    This class contains test cases to verify the behavior of the
    video deletion endpoint.
    """

    def test_delete_video_success(self, client: TestClient):
        """
        Test the successful deletion of a video via the API.

        This test attempts to delete a video with a valid ID. It
        checks that the response status code is 204 (No Content)
        and verifies that no response body is returned.

        Args:
            client (TestClient): The FastAPI test client for sending
                                 requests.
        """
        video_data = {"url": "https://www.example.com/video-to-delete"}
        create_response = client.post("/api/videos/", json=video_data)
        assert create_response.status_code == status.HTTP_201_CREATED
        video_id = create_response.json()["data"]["id"]

        delete_response = client.delete(f"/api/videos/{video_id}")
        assert delete_response.status_code == status.HTTP_204_NO_CONTENT

    def test_delete_video_not_found(self, client: TestClient):
        """
        Test the deletion of a non-existent video via the API.

        This test attempts to delete a video with an ID that does not
        exist in the database. It checks that the API returns a
        404 Not Found status code.

        Args:
            client (TestClient): The FastAPI test client for sending
                                 requests.
        """
        invalid_video_id = "123e4567-e89b-12d3-a456-426614174000"
        delete_response = client.delete(f"/api/videos/{invalid_video_id}")

        assert delete_response.status_code == status.HTTP_404_NOT_FOUND
        assert (
            delete_response.json()["detail"]
            == ErrorMessagesEnum.NO_VIDEOS_FOUND.value
        )

    def test_delete_video_invalid_uuid(self, client: TestClient):
        """
        Test deletion of a video with an invalid UUID format via the API.

        This test attempts to delete a video using an invalid UUID
        (e.g., a string that doesn't conform to UUID standards). It
        checks that the API returns a 400 Bad Request status code
        with an appropriate error message.

        Args:
            client (TestClient): The FastAPI test client for sending
                                 requests.
        """
        invalid_video_id = "invalid-uuid-format"
        delete_response = client.delete(f"/api/videos/{invalid_video_id}")

        assert (
            delete_response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        )
