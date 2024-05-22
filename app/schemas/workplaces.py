from typing import List

from .offices import OfficeIdentifiedSchema

from .base_schema import BaseSchema
from .workplace_types import WorkplaceTypeIdentifiedSchema
from .attributes_schema import AttributeWithValueSchema

from pydantic import Field, AliasChoices


class WorkplaceBaseSchema(BaseSchema):
    wp_address: str = Field(
        ...,
        validation_alias=AliasChoices("wp_address", "address"),
        serialization_alias="address"
    )
    office: OfficeIdentifiedSchema


class WorkplaceIdentifiedSchema(WorkplaceBaseSchema):
    wp_id: int


class WorkplaceWithTypeSchema(WorkplaceIdentifiedSchema):
    type: WorkplaceTypeIdentifiedSchema


class WorkplaceInfoSchema(BaseSchema):
    id: int
    office: OfficeIdentifiedSchema
    address: str
    img_url: str
    type: WorkplaceTypeIdentifiedSchema
    attributes: List[AttributeWithValueSchema]


class WorkplaceCreateSchema(BaseSchema):
    wp_address: str
    wp_img_url: str
    wp_wptype_id: int


class WorkplaceUpdateSchema(WorkplaceCreateSchema):
    wp_id: int


class WorkplaceWithAttributesSchema(WorkplaceCreateSchema):
    wp_attributes_id: List[int]
    