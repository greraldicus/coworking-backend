from pydantic import Field, AliasChoices

from .base_schema import BaseSchema


class PersonBaseSchema(BaseSchema):
    name: str = Field(
        ...,
        validation_alias=AliasChoices('prsn_name', 'name'),
        serialization_alias='name'
    )
    surname: str = Field(
        ...,
        validation_alias=AliasChoices('prsn_surname', 'surname'),
        serialization_alias='surname'
    )


class PersonIdentifiedSchema(PersonBaseSchema):
    id: int = Field(
        ...,
        validation_alias=AliasChoices('prsn_id', 'id'),
        serialization_alias='id'
    )


class PersonWithTenureSchema(PersonBaseSchema):
    tenure: str = Field(
        ...,
        validation_alias=AliasChoices('tenr_title', 'tenure'),
        serialization_alias='tenure'
    )
