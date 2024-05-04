from .api_v1.endpoints import persons_router, auth_router

from fastapi import APIRouter

api_v1_router = APIRouter(prefix="/api_v1")
api_v1_router.include_router(persons_router, tags=["Persons"])
api_v1_router.include_router(auth_router, tags=["JWT Auth"])
