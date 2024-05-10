from fastapi import APIRouter, Depends

from app.auth import encode_jwt, get_user_by_credentials
from app.auth import JwtSchema

auth_router = APIRouter(prefix="/auth")


@auth_router.post(
    path="/login",
    response_model=JwtSchema
)
async def authenticate_user(
    user: JwtSchema = Depends(get_user_by_credentials)
):
    access_token = encode_jwt(payload=user.model_dump())
    return JwtSchema(
        access_token=access_token,
        token_type="Bearer"
    )
