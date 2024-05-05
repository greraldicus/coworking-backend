from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.dal import get_person_with_tenure_schema_by_person_id, create_person_with_tenure_id, get_role_model_by_user_id
from app.schemas import PersonWithTenureSchema, PersonCreateSchema
from app.dependencies import validate_user_by_token_payload

persons_router = APIRouter()


@persons_router.get(
    path="/get_person_info",
    response_model=PersonWithTenureSchema
)
async def get_person_endpoint(
        person_id: int,
        db: Session = Depends(get_db),
        token_user_id: int = Depends(validate_user_by_token_payload)
):
    role = await get_role_model_by_user_id(db=db, user_id=token_user_id)
    if role.rol_title != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return await get_person_with_tenure_schema_by_person_id(db=db, person_id=person_id)


@persons_router.post(
    path="/create_person",
    response_model=int
)
async def create_person_endpoint(
        person_schema: PersonCreateSchema,
        db: Session = Depends(get_db),
        token_user_id: int = Depends(validate_user_by_token_payload)
):
    role = await get_role_model_by_user_id(db=db, user_id=token_user_id)
    if role.rol_title != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return await create_person_with_tenure_id(db=db, person_schema=person_schema)
