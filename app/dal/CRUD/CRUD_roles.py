from .CRUD_base import CRUDBase
from app.db_models import Roles
from app.schemas import RolesUpdateSchema, RolesCreateSchema


class CRUD_Roles(CRUDBase[Roles, RolesCreateSchema, RolesUpdateSchema]):
    pass


crud_roles = CRUD_Roles(Roles)
