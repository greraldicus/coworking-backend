from fastapi_filter.contrib.sqlalchemy import Filter
from typing import List

from sqlalchemy.orm import Session
from watchfiles import awatch

from app.dependencies import get_model_if_valid_id
from app.db_models import Offices
from app.schemas.offices import OfficeIdentifiedSchema, OfficeSearchSchema


async def get_office_model_by_id(db: Session, of_id: int) -> Offices:
    return await get_model_if_valid_id(db=db, model_type=Offices, validating_id=of_id)


async def get_offices_filtered(db: Session, office_filter: Filter) -> List[Offices]:
    return office_filter.filter(db.query(Offices))


async def get_offices_filtered_schema(db: Session, office_filter: Filter) -> List[OfficeSearchSchema]:

    offices_schema_list: List[OfficeSearchSchema] = []

    of_models = await get_offices_filtered(db=db, office_filter=office_filter)
    for of_model in of_models:
        offices_schema_list.append(
            OfficeSearchSchema(
                id=of_model.of_id,
                title=of_model.of_name
            )
        )

    return offices_schema_list
