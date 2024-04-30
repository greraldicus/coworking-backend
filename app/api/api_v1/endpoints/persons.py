from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.db_models import Persons

persons_router = APIRouter()


@persons_router.get(
    path="/TEST_get_person_info",
    response_model=str
)
async def get_person_info(
        person_id: int,
        db: Session = Depends(get_db)
):
    person = db.query(Persons).get(person_id)
    return f"{person.prsn_name}"
