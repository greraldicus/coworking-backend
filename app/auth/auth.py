from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import UserAuthSchema
from app.db_models import Users
from .password_hasher import validate_password


def get_user_by_credentials(
        user_schema: UserAuthSchema,
        db: Session = Depends(get_db)
) -> UserAuthSchema:
    """
    :param user_schema: User login schema
    :param db: Database session
    :return:
    """
    try:
        user_model = db.query(Users).filter(Users.usr_login == user_schema.login).first()
        is_password_valid = validate_password(
            user_schema.password,
            str(user_model.usr_hashed_password).encode()
        )
        if not is_password_valid:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
        return user_schema
    except Exception as err:
        raise err
