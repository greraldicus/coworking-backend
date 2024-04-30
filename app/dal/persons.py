from sqlalchemy.orm import Session

from app.db_models import Persons
from app.dependencies import get_model_if_valid_id
from .tenures import get_tenure_model_by_person_id
from app.schemas import PersonWithTenureSchema


async def get_person_model_by_id(db: Session, person_id: int) -> Persons:
    return await get_model_if_valid_id(db=db, model_type=Persons, validating_id=person_id)


async def get_person_with_tenure_schema_by_person_id(db: Session, person_id: int) -> PersonWithTenureSchema:
    person_model = await get_person_model_by_id(db=db, person_id=person_id)
    person_tenure = await get_tenure_model_by_person_id(db=db, person_id=person_id)

    return PersonWithTenureSchema(
        name=person_model.prsn_name,
        surname=person_model.prsn_surname,
        tenure=person_tenure.tenr_title
    )
