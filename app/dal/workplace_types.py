from sqlalchemy.orm import Session

from app.db_models import WorkplaceTypes
from app.dependencies import get_model_if_valid_id
from app.schemas.workplace_types import WorkplaceTypeCreateSchema


async def get_workplace_types_model_by_id(db: Session, wptype_id: int) -> WorkplaceTypes:
    return await get_model_if_valid_id(db=db, model_type=WorkplaceTypes, validating_id=wptype_id)


async def create_workplace_type(db: Session, create_schema: WorkplaceTypeCreateSchema) -> int:
    wp_type_model = await crud_workplace_types.create(db=db, create_schema=create_schema)
