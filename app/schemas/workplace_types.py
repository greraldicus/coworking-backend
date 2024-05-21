from .base_schema import BaseSchema


class WorkplaceTypeBaseSchema(BaseSchema):
    wptype_title: str


class WorkplaceTypeIdentifiedSchema(WorkplaceTypeBaseSchema):
    wptype_id: int

class WorkplaceTypeCreateSchema(WorkplaceTypeBaseSchema):
    pass

class WorkplaceTypeUpdateSchema(WorkplaceTypeIdentifiedSchema):
    pass