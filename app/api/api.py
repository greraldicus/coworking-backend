from .api_v1.endpoints import persons_router

from fastapi import APIRouter

api_v1_router = APIRouter()
api_v1_router.include_router(persons_router, tags=["Persons"])
