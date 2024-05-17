from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import (
    get_user_by_credentials,
    create_access_token,
    create_refresh_token,
    convert_register_to_create_schema
)
from app.auth import JwtSchema, ROLE_ADMIN
from app.schemas.users_schemas import RegisterSchema
from app.dal.users import create_user
from app.db import get_db
from app.dependencies import get_user_role_by_token_payload

auth_router = APIRouter(prefix="/auth")


@auth_router.post(
    path="/login",
    response_model=JwtSchema,
)
async def authenticate_user(
    user: JwtSchema = Depends(get_user_by_credentials),
    db: Session = Depends(get_db)
):
    access_token = await create_access_token(payload=user.model_dump(), db=db)
    refresh_token = await create_refresh_token(payload=user.model_dump(), db=db)
    return JwtSchema(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer"
    )


@auth_router.post(
    path="/register",
    response_model=int
)
async def registrate_user(
        user_schema: RegisterSchema,
        db: Session = Depends(get_db),
        role: str = Depends(get_user_role_by_token_payload)
):
    if role != ROLE_ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="forbidden")
    return await create_user(db=db, user_schema=convert_register_to_create_schema(user_schema))
