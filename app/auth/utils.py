from datetime import timedelta, datetime

from fastapi import HTTPException, status
import jwt
from jwt.exceptions import ExpiredSignatureError

from .constants import ACCESS_TOKEN_TYPE, REFRESH_TOKEN_TYPE, TOKEN_TYPE_FIELD
from app.core import settings
from app.schemas.users_schemas import RegisterSchema, UserCreateSchema


def get_token_expiration(expire_minutes: int) -> datetime:
    return datetime.utcnow() + timedelta(minutes=expire_minutes)


def add_token_expiration_to_payload(payload: dict, expire_minutes: int) -> dict:
    payload.update(
        iat=datetime.utcnow(),
        exp=get_token_expiration(expire_minutes=expire_minutes)
    )
    return payload


def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    algorithm=settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes
):
    try:
        payload_with_exp = add_token_expiration_to_payload(payload=payload, expire_minutes=expire_minutes)
        encoded = jwt.encode(payload=payload_with_exp, key=private_key, algorithm=algorithm)
        return encoded
    except Exception as err:
        raise err


def decode_jwt(
    token: str,
    public_key: str = settings.auth_jwt.public_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
) -> dict:
    try:
        return jwt.decode(
            token,
            public_key,
            algorithms=[algorithm]
        )
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token has expired')
    except Exception as err:
        raise err


def create_token(
    payload: dict,
    token_type: str,
    expire_minutes: int,
) -> str:
    payload[TOKEN_TYPE_FIELD] = token_type
    return encode_jwt(payload=payload, expire_minutes=expire_minutes)


def create_access_token(
    payload: dict
) -> str:
    return create_token(
        payload=payload,
        token_type=ACCESS_TOKEN_TYPE,
        expire_minutes=settings.auth_jwt.access_token_expire_minutes
    )


def create_refresh_token(
    payload: dict
) -> str:
    return create_token(
        payload=payload,
        token_type=REFRESH_TOKEN_TYPE,
        expire_minutes=settings.auth_jwt.refresh_token_expire_minutes
    )


def convert_register_to_create_schema(register_schema: RegisterSchema) -> UserCreateSchema:
    return UserCreateSchema(
        usr_prsn_id=register_schema.person_id,
        usr_rol_id=register_schema.role_id,
        usr_login=register_schema.login,
        usr_hashed_password=register_schema.password
    )
