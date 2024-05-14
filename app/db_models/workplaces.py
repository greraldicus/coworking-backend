from app.db import Base

from sqlalchemy import Column, Integer, TEXT, ForeignKey
from sqlalchemy.orm import relationship


class Workplaces(Base):
    __tablename__ = "Workplaces"

    wp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    wp_address = Column(TEXT, nullable=False, unique=True)
    wp_wptype_id = Column(Integer, ForeignKey("WorkplaceTypes.wptype_id"), nullable=False)

    wp_wptype = relationship("WorkplaceTypes")
