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


class PersonCreateSchema(BaseSchema):
    prsn_name: str
    prsn_surname: str
    prsn_patronymic: str
    prsn_birth_date: str
    prsn_img_url: str
    prsn_tenr_id: int

    class Config:
        from_attributes = True


class PersonUpdateSchema(PersonCreateSchema):
    pass
