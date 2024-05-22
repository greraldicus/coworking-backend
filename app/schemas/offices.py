from pydantic import Field
from .base_schema import BaseSchema


class OfficeBaseSchema(BaseSchema):
    of_name: str
    of_address: str


class OfficeIdentifiedSchema(OfficeBaseSchema):
    of_id: int


class OfficeSearchSchema(BaseSchema):
    of_id: int = Field(
        ..., 
        alias="id"
    )
    of_name: str = Field(
        ...,
        alias="title"
    )


