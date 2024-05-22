from .api_v1.endpoints import (
    persons_router,
    auth_router,
    tenures_router,
    workplaces_router,
    users_router,
    files_router,
    maps_router
    offices_router
)


from fastapi import APIRouter

api_v1_router = APIRouter(prefix="/api_v1")
api_v1_router.include_router(persons_router, tags=["Persons"])
api_v1_router.include_router(auth_router, tags=["JWT Auth"])
api_v1_router.include_router(tenures_router, tags=["Tenures"])
api_v1_router.include_router(workplaces_router, tags=["Workplaces"])
api_v1_router.include_router(users_router, tags=["Users"])
api_v1_router.include_router(files_router, tags=["Files"])
api_v1_router.include_router(maps_router, tags=["Maps"])
api_v1_router.include_router(offices_router, tags=["Offices"])
