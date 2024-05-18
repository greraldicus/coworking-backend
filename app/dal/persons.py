from typing import List

from sqlalchemy.orm import Session

from app.db_models import Persons, Tenures
from app.dependencies import get_model_if_valid_id
from .tenures import get_tenure_model_by_person_id
from app.schemas import PersonWithTenureSchema, PersonCreateSchema, PersonUpdateSchema, TenureIdentifiedSchema

from .CRUD.CRUD_persons import crud_persons


async def get_all_persons_models(db: Session) -> List[Persons]:
    return db.query(Persons).all()


async def get_person_model_by_id(db: Session, person_id: int) -> Persons:
    return await get_model_if_valid_id(db=db, model_type=Persons, validating_id=person_id)


async def get_person_with_tenure_schema_by_person_id(db: Session, person_id: int) -> PersonWithTenureSchema:
    person_model = await get_person_model_by_id(db=db, person_id=person_id)
    person_tenure = await get_tenure_model_by_person_id(db=db, person_id=person_id)

    return PersonWithTenureSchema(
        prsn_id=person_model.prsn_id,
        name=person_model.prsn_name,
        surname=person_model.prsn_surname,
        patronymic=person_model.prsn_patronymic,
        date_of_birth=person_model.prsn_birth_date,
        tenure=TenureIdentifiedSchema(
            tenr_id=person_tenure.tenr_id,
            tenr_title=person_tenure.tenr_title
        ),
        img_url=person_model.prsn_img_url
    )


async def get_all_persons_with_tenure_schemas(db: Session) -> List[PersonWithTenureSchema]:
    persons_with_tenure_schema: List[PersonWithTenureSchema] = []

    persons_models = await get_all_persons_models(db=db)
    for person_model in persons_models:
        tenure_model = await get_tenure_model_by_person_id(db=db, person_id=person_model.prsn_id)
        persons_with_tenure_schema.append(
            PersonWithTenureSchema(
                prsn_id=person_model.prsn_id,
                name=person_model.prsn_name,
                surname=person_model.prsn_surname,
                patronymic=person_model.prsn_patronymic,
                date_of_birth=person_model.prsn_birth_date,
                tenure=TenureIdentifiedSchema(
                    tenr_id=tenure_model.tenr_id,
                    tenr_title=tenure_model.tenr_title
                ),
                img_url=person_model.prsn_img_url
            )
        )
    return persons_with_tenure_schema


async def create_person_with_tenure_id(db: Session, person_schema: PersonCreateSchema) -> int:
    person_model = await crud_persons.create(db=db, object_create_schema=person_schema)
    return person_model.prsn_id


async def update_person_info(db: Session, person_schema: PersonUpdateSchema) -> None:
    await get_tenure_model_by_person_id(db=db, person_id=person_schema.prsn_id)
    valid_tenure_model = await get_model_if_valid_id(
            db=db,
            model_type=Tenures,
            validating_id=person_schema.prsn_tenr_id
        )
    person_model = await get_person_model_by_id(db=db, person_id=person_schema.prsn_id)
    if valid_tenure_model is not None:
        crud_persons.update(db=db, db_obj=person_model, obj_in=person_schema)
