from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_token_payload
from app.db import get_db


async def validate_user_by_token_payload(
        token_payload: dict = Depends(get_token_payload),
        db: Session = Depends(get_db)
):
    from app.dal import get_user_model_by_id

    if not (user_id := token_payload.get('sub')):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
    if not (user_model := await get_user_model_by_id(db=db, user_id=user_id)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
    return user_model.usr_id


async def get_user_role_by_token_payload(
        valid_user_id: int = Depends(validate_user_by_token_payload),
        db: Session = Depends(get_db)
):
    from app.dal import get_role_model_by_user_id

    role = await get_role_model_by_user_id(db=db, user_id=valid_user_id)
    return role.rol_title
