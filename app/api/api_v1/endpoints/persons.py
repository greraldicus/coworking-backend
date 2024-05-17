from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.dal import (
    get_person_with_tenure_schema_by_person_id,
    get_all_persons_with_tenure_schemas,
    create_person_with_tenure_id,
    update_person_info
)
from app.schemas import PersonWithTenureSchema, PersonCreateSchema, PersonUpdateSchema
from app.dependencies import get_user_role_by_token_payload, get_person_id_by_token_payload
from app.auth import ROLE_ADMIN

persons_router = APIRouter()


@persons_router.get(
    path="/get_persons",
    response_model=List[PersonWithTenureSchema]
)
async def get_person_endpoint(
        db: Session = Depends(get_db),
        role: str = Depends(get_user_role_by_token_payload)
):
    if role != ROLE_ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="forbidden")
    return await get_all_persons_with_tenure_schemas(db=db)


@persons_router.get(
    path="/get_person_info",
    response_model=PersonWithTenureSchema
)
async def get_person_endpoint(
        person_id: int,
        db: Session = Depends(get_db),
        role: str = Depends(get_user_role_by_token_payload)
):
    if role != ROLE_ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="forbidden")
    return await get_person_with_tenure_schema_by_person_id(db=db, person_id=person_id)


@persons_router.get(
    path="/me",
    response_model=PersonWithTenureSchema
)
async def get_person_endpoint(
        db: Session = Depends(get_db),
        person_id: int = Depends(get_person_id_by_token_payload)
):
    return await get_person_with_tenure_schema_by_person_id(db=db, person_id=person_id)


@persons_router.post(
    path="/create_person",
    response_model=int
)
async def create_person_endpoint(
        person_schema: PersonCreateSchema,
        db: Session = Depends(get_db),
        role: str = Depends(get_user_role_by_token_payload)
):
    if role != ROLE_ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="forbidden")
    return await create_person_with_tenure_id(db=db, person_schema=person_schema)


@persons_router.put(
    path="/update_person",
    response_model=None
)
async def update_person_endpoint(
        person_schema: PersonUpdateSchema,
        db: Session = Depends(get_db),
        role: str = Depends(get_user_role_by_token_payload)
):
    if role != ROLE_ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="forbidden")
    return await update_person_info(db=db, person_schema=person_schema)
