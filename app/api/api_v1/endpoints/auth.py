from fastapi import APIRouter, Depends

from app.auth import encode_jwt, get_user_by_credentials
from app.schemas import JwtTokenSchema

auth_router = APIRouter(prefix="/auth")


@auth_router.post(
    path="/login",
    response_model=JwtTokenSchema
)
async def authenticate_user(
    user: JwtTokenSchema = Depends(get_user_by_credentials)
):
    access_token = encode_jwt(payload=user.model_dump())
    return JwtTokenSchema(
        token=access_token,
        token_type="Bearer"
    )
