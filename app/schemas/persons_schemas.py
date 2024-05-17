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
    patronymic: str = Field(
        ...,
        validation_alias=AliasChoices('prsn_patronymic', 'patronymic'),
        serialization_alias='patronymic'
    )
    date_of_birth: str = Field(
        ...,
        validation_alias=AliasChoices('prsn_birth_date', 'date_of_birth'),
        serialization_alias='date_of_birth'
    )
    img_url: str = Field(
        ...,
        validation_alias=AliasChoices('prsn_img_url', 'img_url'),
        serialization_alias='img_url'
    )


class PersonIdentifiedSchema(PersonBaseSchema):
    prsn_id: int = Field(
        ...,
        validation_alias=AliasChoices('prsn_id', 'id'),
        serialization_alias='id'
    )


class PersonWithTenureSchema(PersonIdentifiedSchema):
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
    prsn_id: int
