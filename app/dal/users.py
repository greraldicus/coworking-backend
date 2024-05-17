from sqlalchemy.orm import Session

from app.db_models.users import Users
from app.dependencies import get_model_if_valid_id
from app.schemas.users_schemas import UserCreateSchema, UserUpdateSchema
from app.auth.password_hasher import hash_password

from .CRUD.CRUD_users import crud_users


async def get_user_model_by_id(db: Session, user_id: int) -> Users:
    return await get_model_if_valid_id(db=db, model_type=Users, validating_id=user_id)


async def create_user(db: Session, user_schema: UserCreateSchema) -> Users:
    user_model = await crud_users.create(db=db, object_create_schema=user_schema)
    return user_model.usr_id


async def update_user_credentials(db: Session, user_schema: UserUpdateSchema) -> None:
    user_model = await get_user_model_by_id(db=db, user_id=user_schema.usr_id)
    user_schema.usr_hashed_password = hash_password(user_schema.usr_hashed_password).decode('utf8')
    return crud_users.update(db=db, obj_in=user_schema, db_obj=user_model)
