from fastapi import Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db import get_db
from .jwt_schema import JwtPayloadSchema
from app.db_models import Users
from .password_hasher import validate_password
from .utils import decode_jwt

oauth_2_scheme = OAuth2PasswordBearer(tokenUrl='/api_v1/auth/login')


def get_user_by_credentials(
        username: str = Form(),
        password: str = Form(),
        db: Session = Depends(get_db)
) -> JwtPayloadSchema:
    """
    :param password: password from form
    :param username: username from form
    :param db: Database session
    :return:
    """
    try:
        user_model = db.query(Users).filter(Users.usr_login == username).first()
        if user_model is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect login")
        is_password_valid = validate_password(
            password,
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
    token: str = Depends(oauth_2_scheme)
) -> dict:
    print(token)
    return decode_jwt(token)
