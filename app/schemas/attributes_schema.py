from typing import List

from pydantic import AliasChoices, Field

from .base_schema import BaseSchema


class AttributesBaseSchema(BaseSchema):
    attr_title: str = Field(
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


class AttributeValueByWorkplaceId(BaseSchema):
    attr_id: int
    value: str = Field(
        ...,
        validation_alias=AliasChoices('wpattr_value', 'value'),
        serialization_alias='value'
    )
    wptype_id: int


class WorkplaceAttributesBaseSchema(BaseSchema):
    wpattr_value: str
    wpattr_attr_id: int


class WorkplaceAttributesIdentifiedSchema(WorkplaceAttributesBaseSchema):
    wpattr_id: int


class WorkplaceAttributesCreateSchema(WorkplaceAttributesBaseSchema):
    pass


class WorkplaceAttributesUpdateSchema(WorkplaceAttributesIdentifiedSchema):
    pass


class WorkplaceTypeAttributesBaseSchema(BaseSchema):
    wptypeattr_wpattr_id: int
    wptypeattr_wptype_id: int


class WorkplaceTypeAttributesIdentifiedSchema(WorkplaceTypeAttributesBaseSchema):
    wptypeattr_id: int


class WorkplaceTypeAttributesCreateSchema(WorkplaceTypeAttributesBaseSchema):
    pass


class WorkplaceTypeAttributesUpdateSchema(WorkplaceTypeAttributesIdentifiedSchema):
    pass


class AttributeWithValueSchema(BaseSchema):
    wptypeattr_wp_id: int
    attr_title: str
    attr_value: str
    attr_icon_url: str


class AttributeWithValuesSchema(BaseSchema):
    attr_id: int
    attr_title: str
    values: List[str]
