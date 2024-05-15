from pydantic import ConfigDict

from .base_schema import BaseSchema


class UserAuthSchema(BaseSchema):
    model_config = ConfigDict(strict=True)

    username: str
    password: str


class UserCreateSchema(BaseSchema):
    usr_prsn_id: int
    usr_rol_id: int
    usr_login: str
    usr_hashed_password: str
    

    class Config:
        from_attributes = True


class UserUpdateSchema(UserCreateSchema):
    usr_id: int


class RegisterSchema(BaseSchema):
    person_id: int
    role_id: int
    login: str
    password: str
