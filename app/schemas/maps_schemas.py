from .base_schema import BaseSchema


class MapBaseSchema(BaseSchema):
    mp_title: str
    mp_of_id: int
    mp_layer_img_url: str


class MapIdentifiedSchema(MapBaseSchema):
    mp_id: int
