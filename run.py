from fastapi import FastAPI
from tinyurl_backend import create_app

from tinyurl_backend.views import router

app = create_app()

app.include_router(router)