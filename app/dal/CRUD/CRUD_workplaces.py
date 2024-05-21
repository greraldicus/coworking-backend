from typing import Type

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
        valid_type_model = await get_model_if_valid_id(
            db=db,
            model_type=WorkplaceTypes,
            validating_id=object_create_schema.wp_type.wptype_id
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
