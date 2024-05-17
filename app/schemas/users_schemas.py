from datetime import datetime

from pydantic import Field, AliasChoices
from pydantic import ConfigDict

from .base_schema import BaseSchema


class UserAuthSchema(BaseSchema):
    model_config = ConfigDict(strict=True)

    username: str
    password: str


class UserCreateSchema(BaseSchema):
    usr_prsn_id: int = Field(
        ...,
        validation_alias=AliasChoices("person_id", "usr_prsn_id"),
        alias="person_id"
    )
    usr_rol_id: int = Field(
        ...,
        validation_alias=AliasChoices("role_id", "usr_rol_id"),
        alias="role_id"
    )
    usr_login: str = Field(
        ...,
        validation_alias=AliasChoices("login", "usr_login"),
        alias="login"
    )
    usr_hashed_password: str = Field(
        ...,
        validation_alias=AliasChoices("password", "usr_hashed_password"),
        alias="password"
    )


class UserCreateWithTimestampsSchema(UserCreateSchema):
    usr_last_login: str = Field(default='-')
    usr_created_at: str = Field(default=datetime.utcnow().isoformat())


class UserUpdateSchema(BaseSchema):
    usr_login: str = Field(
        ...,
        alias="login"
    )
    usr_hashed_password: str = Field(
        ...,
        validation_alias=AliasChoices("password", "usr_hashed_password"),
        alias="password"
    )
    usr_id: int = Field(
        ...,
        alias="user_id"
    )


class UserLastLoginUpdateSchema(BaseSchema):
    usr_id: int
    usr_last_login: str


class RegisterSchema(BaseSchema):
    person_id: int
    role_id: int
    login: str
    password: str
