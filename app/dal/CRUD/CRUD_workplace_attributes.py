from typing import Type

from sqlalchemy.orm import Session

from .CRUD_base import CRUDBase
from app.db_models import Attributes, WorkplaceAttributes
from app.dependencies import get_model_if_valid_id
from app.schemas import WorkplaceAttributesCreateSchema, WorkplaceAttributesUpdateSchema


class CRUD_WorkplaceAttribute(
    CRUDBase[
        WorkplaceAttributes,
        WorkplaceAttributesCreateSchema,
        WorkplaceAttributesUpdateSchema
    ]
):
    async def create(
        self,
        db: Session,
        *,
        object_create_schema: WorkplaceAttributesCreateSchema
    ) -> Type[WorkplaceAttributes]:
        valid_tenure_model = await get_model_if_valid_id(
            db=db,
            model_type=Attributes,
            validating_id=object_create_schema.wpattr_attr_id
        )

        if valid_tenure_model is not None:
            return (CRUDBase[WorkplaceAttributes, WorkplaceAttributesCreateSchema, WorkplaceAttributesUpdateSchema]
                    .create(self=self, db=db, object_create_schema=object_create_schema))


crud_workplace_attributes = CRUD_WorkplaceAttribute(WorkplaceAttributes)
