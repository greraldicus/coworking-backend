from sqlalchemy.orm import Session

from app.db_models import Attributes, WorkplaceAttributes
from app.dependencies import get_model_if_valid_id
from app.schemas import WorkplaceAttributesCreateSchema, AttributeValueByWorkplaceId, WorkplaceTypeAttributesBaseSchema
from .CRUD.CRUD_workplace_attributes import crud_workplace_attributes
from .CRUD.CRUD_workplace_type_attributes import crud_workplace_type_attributes


async def get_attribute_model_by_id(db: Session, attr_id: int) -> Attributes:
    return await get_model_if_valid_id(db=db, model_type=Attributes, validating_id=attr_id)


async def create_attribute_value(db: Session, attribute: WorkplaceAttributesCreateSchema) -> WorkplaceAttributes:
    return await crud_workplace_attributes.create(db=db, object_create_schema=attribute)


async def create_attribute_value_by_workplace_type_id(db: Session, attribute: AttributeValueByWorkplaceId) -> int:
    workplace_attribute_value_schema = WorkplaceAttributesCreateSchema(
        wpattr_attr_id=attribute.attr_id,
        wpattr_value=attribute.value
    )
    workplace_attribute_model = await create_attribute_value(db=db, attribute=workplace_attribute_value_schema)
    workplace_type_attributes_schema = WorkplaceTypeAttributesBaseSchema(
        wptypeattr_wpattr_id=workplace_attribute_model.wpattr_id,
        wptypeattr_wptype_id=attribute.wptype_id
    )
    workplace_type_attributes_model = await crud_workplace_type_attributes.create(
        db=db,
        object_create_schema=workplace_type_attributes_schema
    )
    return workplace_type_attributes_model.wptypeattr_id
