from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.handlers.exception_handlers import (
    register_exception_handlers,
)
from src.presentation.routers.router import router
from starlette.responses import RedirectResponse



app = FastAPI(title="Teste Técnico Globo - Backend FastAPI", version="0.0.1", docs_url="/swagger/doc", redoc_url="/swagger/redoc")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

app.include_router(router, prefix="/api")

@app.get("/", tags=["Doc Redirect"])
def redirect():
    return RedirectResponse(url="/swagger/doc")
