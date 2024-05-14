from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dal import (
    get_attribute_model_by_id,
    create_attribute_value_by_workplace_type_id,
    get_attributes_values_list_schema_by_wptype_id,
    get_attribute_with_value_list_schema
)
from app.db import get_db
from app.schemas import (
    AttributesIdentifiedSchema,
    AttributeValueByWorkplaceId,
    AttributeWithValueSchema,
    AttributeWithValuesSchema
)

workplaces_router = APIRouter()


@workplaces_router.get(
    path="/get_attribute",
    response_model=AttributesIdentifiedSchema
)
async def get_attr_endpoint(
    attr_id: int,
    db: Session = Depends(get_db)
):
    return await get_attribute_model_by_id(db=db, attr_id=attr_id)


@workplaces_router.post(
    path="/add_attribute_value_by_workplace_type",
    response_model=int
)
async def add_attribute_value_by_workplace_type_endpoint(
    adding_attribute: AttributeValueByWorkplaceId,
    db: Session = Depends(get_db)
):
    return await create_attribute_value_by_workplace_type_id(db=db, attribute=adding_attribute)


@workplaces_router.get(
    path="/get_attributes_values_by_workplace_type_id",
    response_model=List[AttributeWithValuesSchema]
)
async def get_attributes_values_by_workplace_type_id_endpoint(
    wptype_id: int,
    db: Session = Depends(get_db)
):
    return await get_attributes_values_list_schema_by_wptype_id(db=db, wptype_id=wptype_id)


@workplaces_router.get(
    path="/get_attributes_by_workplace_id",
    response_model=List[AttributeWithValueSchema]
)
async def get_attributes_by_workplace_id(
    wp_id: int,
    db: Session = Depends(get_db)
):
    return await get_attribute_with_value_list_schema(db=db, wp_id=wp_id)
