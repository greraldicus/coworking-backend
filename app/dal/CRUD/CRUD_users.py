import datetime

from sqlalchemy.orm import Session
from .CRUD_base import CRUDBase
from typing import Type
from fastapi import HTTPException, status

from app.auth.password_hasher import hash_password
from app.db_models import Users, Persons, Roles
from app.dependencies import get_model_if_valid_id
from app.schemas.users_schemas import UserCreateSchema, UserUpdateSchema, UserCreateWithTimestampsSchema
from app.auth import ROLE_ADMIN


class CRUD_Users(CRUDBase[Users, UserCreateSchema, UserUpdateSchema]):
    async def create(self, db: Session, *, object_create_schema: UserCreateSchema) -> Type[Users]:

        user = db.query(Users).filter(Users.usr_login == object_create_schema.usr_login).first()
        if user:
            raise HTTPException(status_code=400, detail="User with this login already exists")

        object_create_schema.usr_hashed_password = (
            hash_password(object_create_schema.usr_hashed_password).decode('utf-8')
        )

        valid_person_model = await get_model_if_valid_id(
            db=db,
            validating_id=object_create_schema.usr_prsn_id,
            model_type=Persons
        )
        valid_role_model = await get_model_if_valid_id(
            db=db, 
            validating_id=object_create_schema.usr_rol_id,
            model_type=Roles
        )

        if valid_role_model.rol_title == ROLE_ADMIN:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="forbidden")
        
        if valid_person_model and valid_role_model is not None:
            user_with_timestamps_schema = UserCreateWithTimestampsSchema(
                person_id=valid_person_model.prsn_id,
                role_id=valid_role_model.rol_id,
                login=object_create_schema.usr_login,
                password=object_create_schema.usr_hashed_password,
                usr_last_login='-',
                usr_created_at=datetime.datetime.utcnow().isoformat()
            )

            return (CRUDBase[Persons, UserCreateWithTimestampsSchema, UserUpdateSchema]
                    .create(self=self, db=db, object_create_schema=user_with_timestamps_schema))


crud_users = CRUD_Users(Users)
