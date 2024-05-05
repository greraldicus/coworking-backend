from .base_schema import BaseSchema


class RolesBaseSchema(BaseSchema):
    rol_title: str


class RolesCreateSchema(RolesBaseSchema):
    pass


class RolesUpdateSchema(RolesBaseSchema):
    pass
