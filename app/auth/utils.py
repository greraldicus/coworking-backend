from datetime import timedelta, datetime

import jwt

from app.core import settings


def get_token_expiration(expire_minutes: int) -> datetime:
    return datetime.utcnow() + timedelta(minutes=expire_minutes)


def add_token_expiration_to_payload(payload: dict, expire_minutes: int) -> dict:
    payload.update(
        exp=get_token_expiration(expire_minutes=expire_minutes)
    )
    return payload


def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    algorithm=settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes
):
    payload_with_exp = add_token_expiration_to_payload(payload=payload, expire_minutes=expire_minutes)
    encoded = jwt.encode(payload=payload_with_exp, key=private_key, algorithm=algorithm)
    return encoded


def decode_jwt(
    token: str,
    public_key: str = settings.auth_jwt.public_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
):
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=[algorithm]
    )
    return decoded
