from fastapi import FastAPI
from .routers.v1 import health
app = FastAPI()


app.include_router(health.router)