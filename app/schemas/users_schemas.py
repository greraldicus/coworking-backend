from pydantic import Field, AliasChoices, ConfigDict

from .base_schema import BaseSchema


class UserAuthSchema(BaseSchema):
    model_config = ConfigDict(strict=True)

    login: str
    password: str
