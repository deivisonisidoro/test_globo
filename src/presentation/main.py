from fastapi import FastAPI

from src.presentation.handlers.exception_handlers import (
    register_exception_handlers,
)
from src.presentation.routers.router import router

app = FastAPI()


register_exception_handlers(app)

app.include_router(router, prefix="/api")
