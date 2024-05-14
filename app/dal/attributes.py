from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.db_models import Attributes, WorkplaceAttributes, WorkplaceTypeAttributes
from app.dependencies import get_model_if_valid_id
from app.schemas import (
    WorkplaceAttributesCreateSchema,
    AttributeValueByWorkplaceId,
    WorkplaceTypeAttributesBaseSchema,
    AttributeWithValuesSchema,
    AttributeWithValueSchema
)
from .CRUD.CRUD_workplace_attributes import crud_workplace_attributes
from .CRUD.CRUD_workplace_type_attributes import crud_workplace_type_attributes
from .workplace_types import get_workplace_types_model_by_id
from .workplaces import get_workplace_attributes_intersect_list_models_by_wp_id


async def get_attribute_model_by_id(db: Session, attr_id: int) -> Attributes:
    return await get_model_if_valid_id(db=db, model_type=Attributes, validating_id=attr_id)


async def create_attribute_value(db: Session, attribute: WorkplaceAttributesCreateSchema) -> WorkplaceAttributes:
    try:
        return await crud_workplace_attributes.create(db=db, object_create_schema=attribute)
    except IntegrityError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=err.__repr__())


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


async def get_workplace_type_attribute_by_id(db: Session, wptypeattr_id: int) -> WorkplaceTypeAttributes:
    return await get_model_if_valid_id(db=db, model_type=WorkplaceTypeAttributes, validating_id=wptypeattr_id)


async def get_workplace_type_attributes_by_wptype_id(db: Session, wptype_id: int) -> List[WorkplaceTypeAttributes]:
    workplace_type_attributes = (db.query(WorkplaceTypeAttributes)
                                 .filter(WorkplaceTypeAttributes.wptypeattr_wptype_id == wptype_id)
                                 .all()
                                 )
    return workplace_type_attributes


async def get_workplace_attribute_model_by_id(db: Session, wpattr_id: int) -> WorkplaceAttributes:
    return await get_model_if_valid_id(db=db, model_type=WorkplaceAttributes, validating_id=wpattr_id)


async def get_workplace_attributes_model_list_by_wptype_id(db: Session, wptype_id: int) -> List[WorkplaceAttributes]:
    workplace_attributes: List[WorkplaceAttributes] = []

    workplace_type_attributes = await get_workplace_type_attributes_by_wptype_id(db=db, wptype_id=wptype_id)
    for workplace_type_attribute in workplace_type_attributes:
        workplace_attributes.append(db.query(WorkplaceAttributes).get(workplace_type_attribute.wptypeattr_wpattr_id))

    return workplace_attributes


async def get_workplace_attribute_by_wptypeattr_id(db: Session, wptypeattr_id: int) -> WorkplaceAttributes:
    workplace_type_attribute = await get_workplace_type_attribute_by_id(db=db, wptypeattr_id=wptypeattr_id)
    return await get_workplace_attribute_model_by_id(db=db, wpattr_id=workplace_type_attribute.wptypeattr_wpattr_id)


# НУЖНО РЕФАКТОРИТЬ

async def get_attributes_values_list_schema_by_wptype_id(
        db: Session,
        wptype_id: int
) -> List[AttributeWithValuesSchema]:
    attributes_with_values: List[AttributeWithValuesSchema] = []

    workplace_type_model = await get_workplace_types_model_by_id(db=db, wptype_id=wptype_id)
    workplace_attributes = await get_workplace_attributes_model_list_by_wptype_id(
        db=db,
        wptype_id=workplace_type_model.wptype_id
    )

    workplace_attributes_dict = {}

    for workplace_attribute in workplace_attributes:
        if workplace_attributes_dict.get(workplace_attribute.wpattr_attr_id) is None:
            workplace_attributes_dict[workplace_attribute.wpattr_attr_id] = []
            workplace_attributes_dict[workplace_attribute.wpattr_attr_id].append(workplace_attribute.wpattr_value)
        else:
            workplace_attributes_dict[workplace_attribute.wpattr_attr_id].append(workplace_attribute.wpattr_value)

    for attr_id in workplace_attributes_dict.keys():
        attr_model = await get_attribute_model_by_id(db=db, attr_id=attr_id)
        attributes_with_values.append(
            AttributeWithValuesSchema(
                attr_id=attr_id,
                attr_title=attr_model.attr_title,
                values=workplace_attributes_dict.get(attr_id)
            )
        )

    return attributes_with_values


async def get_attribute_with_value_list_schema(db: Session, wp_id: int) -> List[AttributeWithValueSchema]:
    attributes_with_value_list_schema: List[AttributeWithValueSchema] = []
    workplace_attributes_intersect_models = await get_workplace_attributes_intersect_list_models_by_wp_id(
        db=db,
        wp_id=wp_id
    )

    for workplace_attributes_intersect_model in workplace_attributes_intersect_models:
        workplace_attribute_model = await get_workplace_attribute_by_wptypeattr_id(
            db=db,
            wptypeattr_id=workplace_attributes_intersect_model.wptypeattr_wp_wptypeattr_id
        )
        attribute_model = await get_attribute_model_by_id(db=db, attr_id=workplace_attribute_model.wpattr_attr_id)
        attributes_with_value_list_schema.append(
            AttributeWithValueSchema(
                attr_id=workplace_attribute_model.wpattr_attr_id,
                attr_title=attribute_model.attr_title,
                attr_value=workplace_attribute_model.wpattr_value
            )
        )

    return attributes_with_value_list_schema
