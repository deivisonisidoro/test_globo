from typing import Callable

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.domain.enums.error_messages import ErrorMessagesEnum
from src.domain.exceptions.validation_error.duplicate_url_error import (
    DuplicateUrlError,
)
from src.domain.exceptions.validation_error.invalid_url_error import (
    InvalidUrlError,
)
from src.domain.exceptions.validation_error.video_not_found_error import (
    VideoNotFoundError,
)
from src.domain.exceptions.validation_error.video_validation_error import (
    VideoValidationError,
)


def create_exception_handler(
    status_code: int, initial_detail: str
) -> Callable[[Request, VideoValidationError], JSONResponse]:
    """
    Creates a custom exception handler for FastAPI.

    This function generates a handler that manages exceptions by returning
    a JSON response with a custom error message and status code. It is designed
    for handling specific validation errors in video operations.

    Args:
        status_code (int): The HTTP status code to return with the exception response.
        initial_detail (str): The initial error message to include in the response.

    Returns:
        Callable[[Request, VideoValidationError], JSONResponse]: A custom exception handler
        function that returns a JSONResponse with the provided status code and error message.
    """
    detail = {"message": initial_detail}

    async def exception_handler(
        _: Request, exc: VideoValidationError
    ) -> JSONResponse:
        """
        Handles the actual exception by returning a JSON response with the relevant error message.

        Args:
            _: The incoming request (not used in the function but required by FastAPI).
            exc (VideoValidationError): The exception that was raised during validation.

        Returns:
            JSONResponse: The response containing the error message and status code.
        """
        if exc.message:
            detail["message"] = exc.message

        if exc.name:
            detail["message"] = f"{detail['message']}"

        return JSONResponse(
            status_code=status_code, content={"detail": detail["message"]}
        )

    return exception_handler


def register_exception_handlers(app: FastAPI):
    """
    Registers custom exception handlers to the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    app.add_exception_handler(
        exc_class_or_status_code=DuplicateUrlError,
        handler=create_exception_handler(
            status.HTTP_400_BAD_REQUEST, ErrorMessagesEnum.DUPLICATE_URL.value
        ),
    )
    app.add_exception_handler(
        exc_class_or_status_code=InvalidUrlError,
        handler=create_exception_handler(
            status.HTTP_400_BAD_REQUEST, ErrorMessagesEnum.INVALID_URL.value
        ),
    )
    app.add_exception_handler(
        exc_class_or_status_code=VideoNotFoundError,
        handler=create_exception_handler(
            status.HTTP_404_NOT_FOUND, ErrorMessagesEnum.NO_VIDEOS_FOUND.value
        ),
    )
