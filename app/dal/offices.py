from sqlalchemy.orm import Session

from app.dependencies import get_model_if_valid_id
from app.db_models import Offices


async def get_office_model_by_id(db: Session, of_id: int) -> Offices:
    return await get_model_if_valid_id(db=db, model_type=Offices, validating_id=of_id)
