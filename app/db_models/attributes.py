from app.db import Base

from sqlalchemy import Column, TEXT, Integer


class Attributes(Base):
    __tablename__ = "Attributes"

    attr_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    attr_title = Column(TEXT, nullable=False, unique=True)
