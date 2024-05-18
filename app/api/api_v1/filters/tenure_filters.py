from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional

from app.db_models import Tenures


class TenureFilter(Filter):
    tenr_title__like: Optional[str] = None

    class Constants(Filter.Constants):
        model = Tenures
