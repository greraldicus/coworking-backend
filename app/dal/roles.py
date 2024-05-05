from sqlalchemy.orm import Session

from app.db_models import Roles
from app.dependencies import get_model_if_valid_id
from .users import get_user_model_by_id


async def get_role_model_by_id(db: Session, role_id: int) -> Roles:
    return await get_model_if_valid_id(db=db, model_type=Roles, validating_id=role_id)


async def get_role_model_by_user_id(db: Session, user_id: int) -> Roles:
    user_model = await get_user_model_by_id(db=db, user_id=user_id)
    return await get_role_model_by_id(db=db, role_id=user_model.usr_rol_id)
