from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import UserUpdateSchema, UserAccountSchema
from app.dependencies import get_user_role_by_token_payload
from app.auth import ROLE_ADMIN
from app.dal import update_user_credentials, get_accounts_schemas_by_person_id

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


@users_router.get(
    path="/get_accounts_by_person_id",
    response_model=List[UserAccountSchema]
)
async def update_user_credentials_endpoint(
    person_id: int,
    db: Session = Depends(get_db),
    role: str = Depends(get_user_role_by_token_payload)
):
    if role != ROLE_ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="forbidden")
    return await get_accounts_schemas_by_person_id(db=db, person_id=person_id)
