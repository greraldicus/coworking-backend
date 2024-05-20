from typing import List

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
    wp_id: int
    wp_address: str
    type: WorkplaceTypeIdentifiedSchema
    attributes: List[AttributeWithValueSchema]
