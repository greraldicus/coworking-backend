from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import UserUpdateSchema
from app.dependencies import get_user_role_by_token_payload
from app.auth import ROLE_ADMIN
from app.dal import update_user_credentials

users_router = APIRouter(prefix="/users")


@users_router.put(
    path="/update_user_credentials"
)
async def update_user_credentials_endpoint(
    credentials_schema: UserUpdateSchema,
    db: Session = Depends(get_db),
    role: str = Depends(get_user_role_by_token_payload)
):
    if role != ROLE_ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="forbidden")
    await update_user_credentials(db=db, user_schema=credentials_schema)
