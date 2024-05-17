from fastapi import Depends
from sqlalchemy.orm import Session

from app.db import get_db
from .user_validating import validate_user_by_token_payload


async def get_person_id_by_token_payload(
        valid_user_id: int = Depends(validate_user_by_token_payload),
        db: Session = Depends(get_db)
) -> int:
    from app.dal import get_person_model_by_id, get_user_model_by_id

    user_model = await get_user_model_by_id(db=db, user_id=valid_user_id)
    person_model = await get_person_model_by_id(db=db, person_id=user_model.usr_prsn_id)
    return person_model.prsn_id
