from typing import Type

from sqlalchemy.orm import Session

from app.db_models.workplace_attributes_intersect import WorkplaceAttributesIntersect
from app.db_models.workplace_type_attributes import WorkplaceTypeAttributes
from app.db_models.workplaces import Workplaces
from app.schemas.workplace_attributes_intersect_schemas import WorkplaceAttributesIntersectCreateSchema, WorkplaceAttributesIntersectUpdateSchema

from .CRUD_base import CRUDBase
from app.db_models import Attributes, WorkplaceAttributes
from app.dependencies import get_model_if_valid_id
from app.schemas import WorkplaceAttributesCreateSchema, WorkplaceAttributesUpdateSchema



class CRUD_WorkplaceAttributesIntersect(
    CRUDBase[WorkplaceAttributesIntersect, WorkplaceAttributesIntersectCreateSchema, WorkplaceAttributesIntersectUpdateSchema]
):
    async def create(
        self,
        db: Session,
        *,
        object_create_schema: WorkplaceAttributesIntersectCreateSchema
    ) -> Type[WorkplaceAttributesIntersect]:
        valid_workplace_attributes_model = await get_model_if_valid_id(
            db=db,
            model_type=Workplaces,
            validating_id=object_create_schema.wptypeattr_wp_wp_id
        )

        valid_workplace_types_model = await get_model_if_valid_id(
            db=db,
            model_type=WorkplaceTypeAttributes,
            validating_id=object_create_schema.wptypeattr_wp_wptypeattr_id
        )

        if valid_workplace_attributes_model is not None and valid_workplace_types_model is not None:
            return (CRUDBase[WorkplaceAttributesIntersect,
                            WorkplaceAttributesIntersectCreateSchema,
                            WorkplaceAttributesIntersectUpdateSchema]
                            .create(self=self, db=db, object_create_schema=object_create_schema))


crud_wp_intersect = CRUD_WorkplaceAttributesIntersect(WorkplaceAttributesIntersect)