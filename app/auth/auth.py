from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import UserAuthSchema, JwtPayloadSchema
from app.db_models import Users
from .password_hasher import validate_password
from .utils import decode_jwt

http_bearer = HTTPBearer()


def get_user_by_credentials(
        user_schema: UserAuthSchema,
        db: Session = Depends(get_db)
) -> JwtPayloadSchema:
    """
    :param user_schema: User login schema
    :param db: Database session
    :return:
    """
    try:
        user_model = db.query(Users).filter(Users.usr_login == user_schema.login).first()
        if user_model is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect login")
        is_password_valid = validate_password(
            user_schema.password,
            str(user_model.usr_hashed_password).encode()
        )
        if not is_password_valid:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
        return JwtPayloadSchema(
            sub=user_model.usr_id,
            username=user_model.usr_login
        )
    except Exception as err:
        raise err


def get_token_payload(
    token: HTTPAuthorizationCredentials = Depends(http_bearer)
) -> dict:
    print()
    return decode_jwt(token.credentials)
