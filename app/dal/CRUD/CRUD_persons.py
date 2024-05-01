from .CRUD_base import CRUDBase
from app.db_models import Persons
from app.schemas import PersonCreateSchema, PersonUpdateSchema


class CRUD_Persons(CRUDBase[Persons, PersonCreateSchema, PersonUpdateSchema]):
    pass


crud_persons = CRUD_Persons(Persons)
