from fastapi import FastAPI
from .routers.v1.endpoints import health
app = FastAPI()


app.include_router(health.router)