from .base_schema import BaseSchema


class OfficeBaseSchema(BaseSchema):
    of_name: str
    of_address: str


class OfficeIdentifiedSchema(OfficeBaseSchema):
    of_id: int
