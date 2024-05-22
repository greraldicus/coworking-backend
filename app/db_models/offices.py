from app.db import Base

from sqlalchemy import Column, TEXT, Integer


class Offices(Base):
    __tablename__ = "Offices"

    of_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    of_name = Column(TEXT, nullable=False, unique=True)
    of_address = Column(TEXT, nullable=False)

