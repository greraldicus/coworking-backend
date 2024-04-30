from app.db import Base

from sqlalchemy import Column, TEXT, Integer


class Tenures(Base):
    __tablename__ = "Tenures"

    tenr_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    tenr_title = Column(TEXT, nullable=False)
