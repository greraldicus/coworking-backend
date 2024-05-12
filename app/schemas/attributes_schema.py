from pydantic import AliasChoices, Field

from .base_schema import BaseSchema


class AttributesBaseSchema(BaseSchema):
    title: str = Field(
        ...,
        validation_alias=AliasChoices('attr_title', 'title'),
        serialization_alias='title'
    )


class AttributesIdentifiedSchema(AttributesBaseSchema):
    attr_id: int


class AttributesCreateSchema(AttributesBaseSchema):
    pass


class AttributesUpdateSchema(AttributesIdentifiedSchema):
    pass
