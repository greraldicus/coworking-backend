from typing import Type

from sqlalchemy.orm import Session

from .CRUD_base import CRUDBase
from app.db_models import WorkplaceAttributes, WorkplaceTypeAttributes, WorkplaceTypes
from app.dependencies import get_model_if_valid_id
from app.schemas import WorkplaceTypeAttributesCreateSchema, WorkplaceTypeAttributesUpdateSchema


class CRUD_WorkplaceTypeAttributes(
    CRUDBase[WorkplaceTypeAttributes, WorkplaceTypeAttributesCreateSchema, WorkplaceTypeAttributesUpdateSchema]
):
    async def create(
        self,
        db: Session,
        *,
        object_create_schema: WorkplaceTypeAttributesCreateSchema
    ) -> Type[WorkplaceTypeAttributes]:
        valid_workplace_attributes_model = await get_model_if_valid_id(
            db=db,
            model_type=WorkplaceAttributes,
            validating_id=object_create_schema.wptypeattr_wpattr_id
        )

        valid_workplace_types_model = await get_model_if_valid_id(
            db=db,
            model_type=WorkplaceTypes,
            validating_id=object_create_schema.wptypeattr_wptype_id
        )

        if valid_workplace_attributes_model is not None and valid_workplace_types_model is not None:
            return (CRUDBase[
                        WorkplaceTypeAttributes,
                        WorkplaceTypeAttributesCreateSchema,
                        WorkplaceTypeAttributesUpdateSchema
                    ].create(self=self, db=db, object_create_schema=object_create_schema))


crud_workplace_type_attributes = CRUD_WorkplaceTypeAttributes(WorkplaceTypeAttributes)
