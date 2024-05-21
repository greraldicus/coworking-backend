from typing import List

from app.db_models import workplace_attributes

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


class WorkplaceIdentifiedSchema(WorkplaceBaseSchema):
    wp_id: int


class WorkplaceWithTypeSchema(WorkplaceIdentifiedSchema):
    type: WorkplaceTypeIdentifiedSchema


class WorkplaceInfoSchema(BaseSchema):
    id: int
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
    