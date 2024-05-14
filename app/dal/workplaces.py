from typing import List

from sqlalchemy.orm import Session

from app.db_models import Workplaces, WorkplaceAttributesIntersect
from app.dependencies import get_model_if_valid_id


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
