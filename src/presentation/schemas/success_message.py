from typing import Any, Optional

from pydantic import BaseModel, Field


class SuccessMessageSchema(BaseModel):
    """
    Schema for a success response message.

    This schema defines the structure of the response returned upon successful
    execution of a request. It includes a mandatory success message and optional
    data containing additional information related to the operation.

    Attributes:
        message (str): A required field containing the success message.
        data (Optional[Any]): Optional additional data that can provide extra details
                              related to the operation. The structure of `data` is flexible.
    """

    message: str = Field(..., description="Success message")
    data: Optional[Any] = Field(
        None, description="Optional data related to the success message"
    )
