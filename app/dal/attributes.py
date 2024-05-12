from sqlalchemy.orm import Session

from app.db_models import Attributes
from app.dependencies import get_model_if_valid_id


async def get_attribute_model_by_id(db: Session, attr_id: int) -> Attributes:
    return await get_model_if_valid_id(db=db, model_type=Attributes, validating_id=attr_id)

