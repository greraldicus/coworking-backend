from typing import List

from sqlalchemy.orm import Session

from app.db_models import Workplaces, WorkplaceAttributesIntersect
from app.dependencies import get_model_if_valid_id
from app.schemas import WorkplaceWithTypeSchema, WorkplaceTypeIdentifiedSchema

from .workplace_types import get_workplace_types_model_by_id


async def get_workplace_model_by_id(db: Session, wp_id: int) -> Workplaces:
    return await get_model_if_valid_id(db=db, model_type=Workplaces, validating_id=wp_id)


async def get_workplace_attributes_intersect_list_models_by_wp_id(
    db: Session,
    wp_id: int
) -> List[WorkplaceAttributesIntersect]:
    return (db.query(WorkplaceAttributesIntersect)
            .filter(WorkplaceAttributesIntersect.wptypeattr_wp_wp_id == wp_id)
            .all()
            )


async def get_workplaces_with_type_schemas(db: Session) -> List[WorkplaceWithTypeSchema]:
    workplace_schemas: List[WorkplaceWithTypeSchema] = []

    workplace_models = db.query(Workplaces).all()
    for workplace_model in workplace_models:
        type_model = await get_workplace_types_model_by_id(db=db, wptype_id=workplace_model.wp_wptype_id)
        workplace_schemas.append(
            WorkplaceWithTypeSchema(
                wp_id=workplace_model.wp_id,
                wp_address=workplace_model.wp_address,
                type=WorkplaceTypeIdentifiedSchema(
                    wptype_id=type_model.wptype_id,
                    wptype_title=type_model.wptype_title
                )
            )
        )

    return workplace_schemas
