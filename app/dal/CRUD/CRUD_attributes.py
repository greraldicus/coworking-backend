from .CRUD_base import CRUDBase

from app.db_models import Attributes
from app.schemas import AttributesUpdateSchema, AttributesCreateSchema


class CRUDAttributes(CRUDBase[Attributes, AttributesUpdateSchema, AttributesCreateSchema]):
    pass


crud_attributes = CRUDAttributes(Attributes)
