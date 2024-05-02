from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.dal import get_person_with_tenure_schema_by_person_id, create_person_with_tenure_id
from app.schemas import PersonWithTenureSchema, PersonCreateSchema

persons_router = APIRouter()


@persons_router.get(
    path="/get_person_info",
    response_model=PersonWithTenureSchema
)
async def get_person_endpoint(
        person_id: int,
        db: Session = Depends(get_db)
):
    return await get_person_with_tenure_schema_by_person_id(db=db, person_id=person_id)


@persons_router.post(
    path="/create_person",
    response_model=int
)
async def create_person_endpoint(
        person_schema: PersonCreateSchema,
        db: Session = Depends(get_db)
):
    return await create_person_with_tenure_id(db=db, person_schema=person_schema)
