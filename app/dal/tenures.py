from typing import List

from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db_models.tenures import Tenures
from app.dependencies import get_model_if_valid_id
from app.schemas.tenures_schemas import TenureBaseSchema, TenureCreateSchema, TenureIdentifiedSchema

from .CRUD.CRUD_tenures import crud_tenures


async def get_tenure_model_by_id(db: Session, tenure_id: int) -> Tenures:
    return await get_model_if_valid_id(db=db, model_type=Tenures, validating_id=tenure_id)


async def get_tenure_model_by_person_id(db: Session, person_id: int) -> Tenures:
    from .persons import get_person_model_by_id

    person_model = await get_person_model_by_id(db=db, person_id=person_id)
    return await get_tenure_model_by_id(db=db, tenure_id=person_model.prsn_tenr_id)


async def create_tenure(db: Session, tenure_schema: TenureCreateSchema) -> int:
    tenure_model = crud_tenures.create(db=db, object_create_schema=tenure_schema)
    return tenure_model.tenr_id


async def get_tenure_base_schema_by_id(db: Session, tenure_id: int) -> TenureBaseSchema:
    tenure_model = await get_tenure_model_by_id(db=db, tenure_id=tenure_id)
    return TenureBaseSchema(tenr_title=tenure_model.tenr_title)


async def get_tenures_filtered(db: Session, tenure_filter: Filter) -> List[TenureIdentifiedSchema]:
    return tenure_filter.filter(db.query(Tenures))
