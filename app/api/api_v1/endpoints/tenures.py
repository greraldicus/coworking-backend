from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dal import get_tenure_base_schema_by_id, create_tenure
from app.db import get_db
from app.schemas.tenures_schemas import TenureBaseSchema, TenureCreateSchema

tenures_router = APIRouter()


@tenures_router.get(
    path="/get_tenure_info",
    response_model=TenureBaseSchema
)
async def get_tenure_endpoint(
        tenure_id: int,
        db: Session = Depends(get_db)
):
    return await get_tenure_base_schema_by_id(db=db, tenure_id=tenure_id)


@tenures_router.post(
    path="/create_tenure",
    response_model=int
)
async def create_tenure_endpoint(
        tenure_schema: TenureCreateSchema,
        db: Session = Depends(get_db)
):
    return await create_tenure(db=db, tenure_schema=tenure_schema)
