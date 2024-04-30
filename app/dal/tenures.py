from sqlalchemy.orm import Session

from app.db_models import Tenures
from app.dependencies import get_model_if_valid_id


async def get_tenure_model_by_id(db: Session, tenure_id: int) -> Tenures:
    return await get_model_if_valid_id(db=db, model_type=Tenures, validating_id=tenure_id)


async def get_tenure_model_by_person_id(db: Session, person_id: int) -> Tenures:
    from .persons import get_person_model_by_id

    person_model = await get_person_model_by_id(db=db, person_id=person_id)
    return await get_tenure_model_by_id(db=db, tenure_id=person_model.prsn_tenr_id)
