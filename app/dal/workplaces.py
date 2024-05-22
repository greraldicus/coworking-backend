from typing import List

from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy.orm import Session

from app.db_models import Workplaces, WorkplaceAttributesIntersect
from app.db_models.workplace_type_attributes import WorkplaceTypeAttributes
from app.dependencies import get_model_if_valid_id
from app.schemas import (
    WorkplaceWithTypeSchema,
    WorkplaceTypeIdentifiedSchema,
    WorkplaceInfoSchema,
    AttributeWithValueSchema,
    WorkplaceAttributesIntersectCreateSchema,
    WorkplaceWithAttributesSchema, OfficeIdentifiedSchema
)
from app.schemas.attributes_schema import WorkplaceTypeAttributesCreateSchema
from app.schemas.workplaces import WorkplaceCreateSchema

from .workplace_types import get_workplace_types_model_by_id

from .CRUD.CRUD_workplaces import crud_workplaces
from .CRUD.CRUD_workplace_attributes_intersect import crud_wp_intersect
from .CRUD.CRUD_workplace_type_attributes import crud_workplace_type_attributes


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


async def get_workplace_attributes_intersect_model_by_id(
    db: Session,
    wptypeattr_wp_id: int
) -> WorkplaceAttributesIntersect:
    return await get_model_if_valid_id(db=db, model_type=WorkplaceAttributesIntersect, validating_id=wptypeattr_wp_id)


async def get_workplaces_with_type_schemas(db: Session) -> List[WorkplaceWithTypeSchema]:
    from .offices import get_office_model_by_id

    workplace_schemas: List[WorkplaceWithTypeSchema] = []

    workplace_models = db.query(Workplaces).all()
    for workplace_model in workplace_models:
        office_model = await get_office_model_by_id(db=db, of_id=workplace_model.wp_of_id)
        type_model = await get_workplace_types_model_by_id(db=db, wptype_id=workplace_model.wp_wptype_id)
        workplace_schemas.append(
            WorkplaceWithTypeSchema(
                wp_id=workplace_model.wp_id,
                wp_address=workplace_model.wp_address,
                type=WorkplaceTypeIdentifiedSchema(
                    wptype_id=type_model.wptype_id,
                    wptype_title=type_model.wptype_title
                ),
                office=OfficeIdentifiedSchema(
                    of_id=office_model.of_id,
                    of_address=office_model.of_address,
                    of_name=office_model.of_name
                ),
                wp_x_coord=workplace_model.wp_x_coord,
                wp_y_coord=workplace_model.wp_y_coord,
                wp_mp_id=workplace_model.wp_mp_id
            )
        )

    return workplace_schemas


async def get_workplace_info_schema(db: Session, wp_id: int) -> WorkplaceInfoSchema:
    from .attributes import get_attribute_with_value_list_schema
    from .offices import get_office_model_by_id

    workplace_model = await get_workplace_model_by_id(db=db, wp_id=wp_id)
    type_model = await get_workplace_types_model_by_id(db=db, wptype_id=workplace_model.wp_wptype_id)
    attribute_schemas = await get_attribute_with_value_list_schema(db=db, wp_id=workplace_model.wp_id)
    office_model = await get_office_model_by_id(db=db, of_id=workplace_model.wp_of_id)

    workplace_info_schema = WorkplaceInfoSchema(
        id=workplace_model.wp_id,
        address=workplace_model.wp_address,
        img_url=workplace_model.wp_img_url,
        type=WorkplaceTypeIdentifiedSchema(
            wptype_id=type_model.wptype_id,
            wptype_title=type_model.wptype_title
        ),
        office=OfficeIdentifiedSchema(
            of_id=office_model.of_id,
            of_address=office_model.of_address,
            of_name=office_model.of_name
        ),
        attributes=[]
    )

    for attribute_schema in attribute_schemas:
        workplace_info_schema.attributes.append(
            AttributeWithValueSchema(
                attr_icon_url=attribute_schema.attr_icon_url,
                wptypeattr_wp_id=attribute_schema.wptypeattr_wp_id,
                attr_title=attribute_schema.attr_title,
                attr_value=attribute_schema.attr_value
            )
        )

    return workplace_info_schema


async def get_workplace_type_attributes_by_id(db: Session, wptypeattr_id: int) -> WorkplaceTypeAttributes:
    return await get_model_if_valid_id(db=db, model_type=WorkplaceTypeAttributes, validating_id=wptypeattr_id)
    

async def create_workplace(db: Session, workplace_create_schema: WorkplaceCreateSchema) -> Workplaces:
    from .offices import get_office_model_by_id

    await get_office_model_by_id(db=db, of_id=workplace_create_schema.wp_of_id)
    workplace_model = await crud_workplaces.create(db=db, object_create_schema=workplace_create_schema)
    return workplace_model


async def create_workplace_intersect(db: Session, wp_int_schema: WorkplaceAttributesIntersectCreateSchema) -> int:
    wp_int_model = await crud_wp_intersect.create(db=db, object_create_schema=wp_int_schema)
    return wp_int_model.wptypeattr_wp_wptypeattr_id


async def create_workplace_type_attributes(
        db: Session, wp_type_attr_schema:
        WorkplaceTypeAttributesCreateSchema
) -> int:
    wp_type_attr_model = await crud_workplace_type_attributes.create(db=db, object_create_schema=wp_type_attr_schema)
    return wp_type_attr_model.wptypeattr_id


async def create_workplace_with_attributes(db: Session, create_schema: WorkplaceWithAttributesSchema):
    workplace_model = await create_workplace(
        db=db,
        workplace_create_schema=WorkplaceCreateSchema(
            wp_address=create_schema.wp_address,
            wp_img_url=create_schema.wp_img_url,
            wp_wptype_id=create_schema.wp_wptype_id,
            wp_of_id=create_schema.wp_of_id,
            wp_mp_id=create_schema.wp_mp_id,
            wp_y_coord=create_schema.wp_y_coord,
            wp_x_coord=create_schema.wp_x_coord
        )
    )
    
    for wptypeattr_id in create_schema.wp_attributes_id:
        wptypeattr_model = await get_workplace_type_attributes_by_id(db=db, wptypeattr_id=wptypeattr_id)
        await create_workplace_intersect(
            db=db,
            wp_int_schema=WorkplaceAttributesIntersectCreateSchema(
                wptypeattr_wp_wp_id=workplace_model.wp_id,
                wptypeattr_wp_wptypeattr_id=wptypeattr_model.wptypeattr_id
            )
        )  
    return workplace_model.wp_id


async def delete_workplace_by_id(db: Session, workplace_id: int) -> None:
    valid_workplace_model = await get_workplace_model_by_id(db=db, wp_id=workplace_id)
    attributes_intersect_models = await get_workplace_attributes_intersect_list_models_by_wp_id(
        db=db,
        wp_id=valid_workplace_model.wp_id
    )
    for attributes_intersect_model in attributes_intersect_models:
        crud_wp_intersect.remove(db=db, entity_id=attributes_intersect_model.wptypeattr_wp_id)

    crud_workplaces.remove(db=db, entity_id=valid_workplace_model.wp_id)


async def delete_attribute_intersect_by_id(db: Session, wptypeattr_wp_id: int) -> None:
    valid_intersect_model = await get_workplace_attributes_intersect_model_by_id(
        db=db,
        wptypeattr_wp_id=wptypeattr_wp_id
    )
    crud_wp_intersect.remove(db=db, entity_id=valid_intersect_model.wptypeattr_wp_id)


async def get_workplaces_filtered(db: Session, workplace_filter: Filter) -> List[WorkplaceWithTypeSchema]:
    from .offices import get_office_model_by_id

    workplace_schemas: List[WorkplaceWithTypeSchema] = []

    workplace_models: List[Workplaces] = workplace_filter.filter(db.query(Workplaces))

    for workplace_model in workplace_models:
        office_model = await get_office_model_by_id(db=db, of_id=workplace_model.wp_of_id)
        type_model = await get_workplace_types_model_by_id(db=db, wptype_id=workplace_model.wp_wptype_id)
        workplace_schemas.append(
            WorkplaceWithTypeSchema(
                wp_id=workplace_model.wp_id,
                wp_address=workplace_model.wp_address,
                type=WorkplaceTypeIdentifiedSchema(
                    wptype_id=type_model.wptype_id,
                    wptype_title=type_model.wptype_title
                ),
                office=OfficeIdentifiedSchema(
                    of_id=office_model.of_id,
                    of_address=office_model.of_address,
                    of_name=office_model.of_name
                ),
                wp_x_coord=workplace_model.wp_x_coord,
                wp_y_coord=workplace_model.wp_y_coord,
                wp_mp_id=workplace_model.wp_mp_id
            )
        )

    return workplace_schemas
