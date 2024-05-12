from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dal import get_attribute_model_by_id
from app.db import get_db
from app.schemas import AttributesIdentifiedSchema

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
