from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional

from app.db_models import Workplaces


class WorkplaceAddressFilter(Filter):
    wp_address__like: Optional[str] = None

    class Constants(Filter.Constants):
        model = Workplaces