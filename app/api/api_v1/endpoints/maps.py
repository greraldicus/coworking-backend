from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.dal import get_maps_schemas_by_office_id

maps_router = APIRouter(prefix="/maps")


@maps_router.get(
    path="/get_maps_by_office_id"
)
async def get_maps_by_office_id_endpoint(
    office_id: int,
    db: Session = Depends(get_db)
):
    return await get_maps_schemas_by_office_id(db=db, office_id=office_id)
