from typing import List

from sqlalchemy.orm import Session

from app.dal import get_office_model_by_id
from app.schemas import MapIdentifiedSchema
from app.db_models import Maps


async def get_maps_models_by_office_id(db: Session, office_id: int) -> List[Maps]:
    valid_office_model = await get_office_model_by_id(db=db, of_id=office_id)
    return db.query(Maps).filter(Maps.mp_of_id == valid_office_model.of_id).all()


async def get_maps_schemas_by_office_id(db: Session, office_id: int) -> List[MapIdentifiedSchema]:
    maps_schemas: List[MapIdentifiedSchema] = []

    maps_models = await get_maps_models_by_office_id(db=db, office_id=office_id)

    for map_model in maps_models:
        maps_schemas.append(map_model)

    return maps_schemas
