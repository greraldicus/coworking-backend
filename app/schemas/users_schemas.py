from pydantic import ConfigDict

from .base_schema import BaseSchema


class UserAuthSchema(BaseSchema):
    model_config = ConfigDict(strict=True)

    username: str
    password: str
