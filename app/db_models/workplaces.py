from app.db import Base

from sqlalchemy import Column, Integer, TEXT, ForeignKey
from sqlalchemy.orm import relationship


class Workplaces(Base):
    __tablename__ = "Workplaces"

    wp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    wp_address = Column(TEXT, nullable=False, unique=True)
    wp_img_url = Column(TEXT, nullable=False)
    wp_wptype_id = Column(Integer, ForeignKey("WorkplaceTypes.wptype_id"), nullable=False)
    wp_of_id = Column(Integer, ForeignKey("Offices.of_id"), nullable=False)
    wp_mp_id = Column(Integer, ForeignKey("Maps.mp_id"), nullable=False)
    wp_x_coord = Column(TEXT, nullable=False)
    wp_y_coord = Column(TEXT, nullable=False)

    wp_wptype = relationship("WorkplaceTypes")
    wp_of = relationship("Offices")
    wp_mp = relationship("Maps")
