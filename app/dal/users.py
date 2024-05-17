from typing import List

from sqlalchemy.orm import Session

from app.db_models.users import Users
from app.dependencies import get_model_if_valid_id
from app.schemas.users_schemas import UserCreateSchema, UserUpdateSchema, UserLastLoginUpdateSchema, UserAccountSchema
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


async def update_user_last_login_timestamp(db: Session, schema: UserLastLoginUpdateSchema) -> None:
    user_model = await get_user_model_by_id(db=db, user_id=schema.usr_id)
    return crud_users.update(db=db, obj_in=schema, db_obj=user_model)


async def get_user_models_by_person_id(db: Session, person_id: int) -> List[Users]:
    from app.dal import get_person_model_by_id

    person_model = await get_person_model_by_id(db=db, person_id=person_id)
    return db.query(Users).filter(Users.usr_prsn_id == person_model.prsn_id).all()


async def get_accounts_schemas_by_person_id(db: Session, person_id: int) -> List[UserAccountSchema]:
    from app.dal import get_role_model_by_id

    accounts_schema_list: List[UserAccountSchema] = []

    accounts = await get_user_models_by_person_id(db=db, person_id=person_id)
    for account in accounts:
        role_model = await get_role_model_by_id(db=db, role_id=account.usr_rol_id)

        accounts_schema_list.append(
            UserAccountSchema(
                user_id=account.usr_id,
                login=account.usr_login,
                role=role_model.rol_title,
                created_at=account.usr_created_at,
                last_login=account.usr_last_login
            )
        )

    return accounts_schema_list
