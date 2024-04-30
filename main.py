from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import api_v1_router

app = FastAPI(
    title="Coworking Booking System API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True,
        port=8085,
        host="0.0.0.0"
    )
