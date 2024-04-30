from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.dal import get_person_with_tenure_schema_by_person_id
from app.schemas import PersonWithTenureSchema

persons_router = APIRouter()


@persons_router.get(
    path="/get_person_info",
    response_model=PersonWithTenureSchema
)
async def get_person_info(
        person_id: int,
        db: Session = Depends(get_db)
):
    return await get_person_with_tenure_schema_by_person_id(db=db, person_id=person_id)
