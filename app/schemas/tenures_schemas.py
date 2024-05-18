from .base_schema import BaseSchema


class TenureBaseSchema(BaseSchema):
    tenr_title: str


class TenureIdentifiedSchema(TenureBaseSchema):
    tenr_id: int


class TenureCreateSchema(TenureBaseSchema):
    pass

    class Config:
        from_attributes = True


class TenureUpdateSchema(TenureCreateSchema):
    tenr_id: int
