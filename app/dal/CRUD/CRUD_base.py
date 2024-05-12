from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError

from app.exceptions import CrudBaseExc

ModelType = TypeVar("ModelType", bound=Any)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, req_id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == req_id).first()

    def get_all(self, db: Session, *, skip: int = 0, limit: int) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def update(
            self,
            db: Session,
            *,
            db_obj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        try:
            obj_data = jsonable_encoder(db_obj)
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.model_dump(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
            db.add(db_obj)
            db.flush()
            db.refresh(db_obj)
            db.commit()
            return db_obj
        except IntegrityError as err:
            raise err

        except Exception:
            raise CrudBaseExc(
                message="cannot update record in",
                entity_name=self.model.__name__,
                entity_id=obj_in.model_dump()[inspect(self.model).primary_key[0].name]
            )

    def create(self, db: Session, *, object_create_schema: CreateSchemaType) -> ModelType:
        try:
            obj_in_data = jsonable_encoder(object_create_schema)
            if isinstance(object_create_schema, dict):
                create_data = obj_in_data
            else:
                create_data = object_create_schema.model_dump(exclude_unset=True)

            db_obj = self.model(**create_data)
            db.add(db_obj)
            db.flush()
            db.refresh(db_obj)
            db.commit()
            return db_obj
        except IntegrityError as err:
            raise err

        except Exception as err:
            raise CrudBaseExc(
                message=f"cannot create record with error: {err.__repr__()} in",
                entity_name=self.model.__name__
            )

    def remove(self, db: Session, *, entity_id: int) -> ModelType:
        try:
            obj = db.query(self.model).get(entity_id)
            db.delete(obj)
            db.flush()
            return obj
        except IntegrityError as err:
            raise err

        except Exception:
            raise CrudBaseExc(
                message="невозможно удалить запись в",
                entity_name=self.model.__name__,
                entity_id=entity_id
            )

    def get_by_criterion(self, db: Session, *, criterion: bool) -> list[ModelType]:
        return db.query(self.model).filter(criterion).all()

    def get_by_criteria(self, db: Session, *, criteria: list[bool]) -> list[ModelType]:
        query = db.query(self.model)
        for criterion in criteria:
            query = query.filter(criterion)
        return query.all()
