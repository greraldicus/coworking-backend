from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional

from app.db_models.offices import Offices


class OfficeFilter(Filter):
    of_name__like: Optional[str] = None

    class Constants(Filter.Constants):
        model = Offices