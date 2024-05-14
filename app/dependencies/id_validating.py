from typing import TypeVar, Any, Type

from fastapi import HTTPException, status
from sqlalchemy.orm import Session


ModelType = TypeVar("ModelType", bound=Any)


async def get_model_if_valid_id(
        db: Session,
        validating_id: int,
        model_type: Type[ModelType]
) -> ModelType:
    try:
        model_obj = db.query(model_type).get(validating_id)
        if model_obj is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"{model_type.__tablename__} with id={validating_id} does not exist, id is NOT valid."
            )
        return model_obj
    except Exception as err:
        raise err