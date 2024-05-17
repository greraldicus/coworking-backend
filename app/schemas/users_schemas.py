from pydantic import Field, AliasChoices

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


class UserUpdateSchema(BaseSchema):
    usr_login: str
    usr_hashed_password: str = Field(
        ...,
        validation_alias=AliasChoices("password", "usr_hashed_password"),
        alias="password"
    )
    usr_id: int


class RegisterSchema(BaseSchema):
    person_id: int
    role_id: int
    login: str
    password: str
