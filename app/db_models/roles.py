from app.db import Base

from sqlalchemy import Column, TEXT, Integer


class Roles(Base):
    __tablename__ = "Roles"

    rol_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    rol_title = Column(TEXT, nullable=False)
    