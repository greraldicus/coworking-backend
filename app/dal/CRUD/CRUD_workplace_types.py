from typing import Type

from sqlalchemy.orm import Session

from app.schemas import WorkplaceTypeCreateSchema, WorkplaceTypeUpdateSchema

from .CRUD_base import CRUDBase
from app.db_models import WorkplaceTypes


class CRUD_WorkplaceTypes(CRUDBase[WorkplaceTypes, WorkplaceTypeCreateSchema, WorkplaceTypeUpdateSchema]):
    async def create(self, db: Session, *, object_create_schema: WorkplaceTypeCreateSchema) -> Type[WorkplaceTypes]:
            return (
                CRUDBase[
                    WorkplaceTypes,
                    WorkplaceTypeCreateSchema, 
                    WorkplaceTypeUpdateSchema
                ]
                .create(self=self, db=db, object_create_schema=object_create_schema)
            )


crud_workplace_types = CRUD_WorkplaceTypes(WorkplaceTypes)
