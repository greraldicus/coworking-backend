from typing import Type

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.db_models.workplace_types import WorkplaceTypes
from app.db_models.workplaces import Workplaces

from .CRUD_base import CRUDBase
from app.dependencies import get_model_if_valid_id
from app.schemas import WorkplaceCreateSchema, WorkplaceUpdateSchema


class CRUD_Workplaces(CRUDBase[Workplaces, WorkplaceCreateSchema, WorkplaceUpdateSchema]):
    async def create(
        self,
        db: Session,
        *,
        object_create_schema: WorkplaceCreateSchema
    ) -> Type[Workplaces]:
        workplace_model = db.query(Workplaces).filter(Workplaces.wp_address == object_create_schema.wp_address).first()
        if workplace_model:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Workplace with same address already exist"
            )

        valid_type_model = await get_model_if_valid_id(
            db=db,
            model_type=WorkplaceTypes,
            validating_id=object_create_schema.wp_wptype_id
        )
        if valid_type_model is not None:
            return (
                CRUDBase[
                    Workplaces,
                    WorkplaceCreateSchema,
                    WorkplaceUpdateSchema
                ]
                .create(self=self, db=db, object_create_schema=object_create_schema)
            )


crud_workplaces = CRUD_Workplaces(Workplaces)
