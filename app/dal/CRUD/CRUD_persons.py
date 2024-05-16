from typing import Type

from fastapi import HTTPException
from sqlalchemy.orm import Session

from .CRUD_base import CRUDBase
from app.db_models import Persons, Tenures
from app.dependencies import get_model_if_valid_id
from app.schemas import PersonCreateSchema, PersonUpdateSchema


class CRUD_Persons(CRUDBase[Persons, PersonCreateSchema, PersonUpdateSchema]):
    async def create(self, db: Session, *, object_create_schema: PersonCreateSchema) -> Type[Persons]:
        valid_tenure_model = await get_model_if_valid_id(
            db=db,
            model_type=Tenures,
            validating_id=object_create_schema.prsn_tenr_id
        )

        if valid_tenure_model is not None:
            return (CRUDBase[Persons, PersonCreateSchema, PersonUpdateSchema]
                    .create(self=self, db=db, object_create_schema=object_create_schema))


crud_persons = CRUD_Persons(Persons)
