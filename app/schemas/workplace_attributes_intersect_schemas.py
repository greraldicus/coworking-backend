from .base_schema import BaseSchema


class WorkplaceAttributesIntersectBaseSchema(BaseSchema):
    wptypeattr_wp_wptypeattr_id: int
    wptypeattr_wp_wp_id: int


class WorkplaceAttributesIntersectIdentifiedSchema(WorkplaceAttributesIntersectBaseSchema):
    wptypeattr_wp_id: int


class WorkplaceAttributesIntersectCreateSchema(WorkplaceAttributesIntersectBaseSchema):
    pass


class WorkplaceAttributesIntersectUpdateSchema(WorkplaceAttributesIntersectIdentifiedSchema):
    pass
