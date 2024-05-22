from typing import List

from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from sqlalchemy.orm import Session

from app.api.api_v1.filters.office_filters import OfficeFilter
from app.dal.offices import get_offices_filtered_schema
from app.db.session import get_db
from app.schemas.offices import OfficeSearchSchema
from fastapi_filter.contrib.sqlalchemy import Filter


offices_router = APIRouter(prefix="/offices")


@offices_router.get(
    path="/get_offices",
    response_model=List[OfficeSearchSchema]
)
async def get_offices_filtered_endpoint(
        db: Session = Depends(get_db),
        office_filter: Filter = FilterDepends(OfficeFilter)
):
    return await get_offices_filtered_schema(db=db, office_filter=office_filter)