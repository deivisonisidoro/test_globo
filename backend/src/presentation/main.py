from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.handlers.exception_handlers import (
    register_exception_handlers,
)
from src.presentation.routers.router import router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

app.include_router(router, prefix="/api")
