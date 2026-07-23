from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="DataScope API",
    description="Backend API for the DataScope Job Analytics Platform",
    version="1.0.0"
)

app.include_router(router)