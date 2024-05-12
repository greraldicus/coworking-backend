from .CRUD_base import CRUDBase

from app.db_models import Tenures
from app.schemas.tenures_schemas import TenureUpdateSchema, TenureCreateSchema


class CRUDTenures(CRUDBase[Tenures, TenureUpdateSchema, TenureCreateSchema]):
    pass


crud_tenures = CRUDTenures(Tenures)
