from sqlalchemy.orm import Session

from app.db_models.users import Users
from app.dependencies import get_model_if_valid_id
from app.schemas.users_schemas import UserCreateSchema

from .CRUD.CRUD_users import crud_users


async def get_user_model_by_id(db: Session, user_id: int) -> Users:
    return await get_model_if_valid_id(db=db, model_type=Users, validating_id=user_id)


async def create_user(db: Session, user_schema: UserCreateSchema) -> Users:
    user_model = await crud_users.create(db=db, object_create_schema=user_schema)
    return user_model.usr_id
