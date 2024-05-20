from .base_schema import BaseSchema
from .workplace_types import WorkplaceTypeIdentifiedSchema

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
