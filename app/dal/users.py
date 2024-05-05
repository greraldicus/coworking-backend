from sqlalchemy.orm import Session

from app.db_models import Users
from app.dependencies import get_model_if_valid_id


async def get_user_model_by_id(db: Session, user_id: int) -> Users:
    return await get_model_if_valid_id(db=db, model_type=Users, validating_id=user_id)
