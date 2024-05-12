from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dal import get_attribute_model_by_id, create_attribute_value_by_workplace_type_id
from app.db import get_db
from app.schemas import AttributesIdentifiedSchema, AttributeValueByWorkplaceId

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
async def add_attribute_value_by_workplace_type(
    adding_attribute: AttributeValueByWorkplaceId,
    db: Session = Depends(get_db)
):
    return await create_attribute_value_by_workplace_type_id(db=db, attribute=adding_attribute)
