from fastapi import APIRouter, Depends

from app.auth import get_user_by_credentials, create_access_token, create_refresh_token
from app.auth import JwtSchema

auth_router = APIRouter(prefix="/auth")


@auth_router.post(
    path="/login",
    response_model=JwtSchema
)
async def authenticate_user(
    user: JwtSchema = Depends(get_user_by_credentials)
):
    access_token = create_access_token(user.model_dump())
    refresh_token = create_refresh_token(user.model_dump())
    return JwtSchema(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer"
    )
