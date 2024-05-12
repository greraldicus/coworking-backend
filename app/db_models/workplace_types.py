from app.db import Base

from sqlalchemy import Column, Integer, TEXT


class WorkplaceTypes(Base):
    __tablename__ = "WorkplaceTypes"

    wptype_title = Column(TEXT, nullable=False, unique=True)
    wptype_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
