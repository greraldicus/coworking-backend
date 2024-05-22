from app.db import Base

from sqlalchemy import Column, TEXT, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Maps(Base):
    __tablename__ = "Maps"

    mp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    mp_title = Column(TEXT, nullable=False)
    mp_of_id = Column(Integer, ForeignKey("Offices.of_id"), nullable=False)
    mp_layer_img_url = Column(TEXT, nullable=False)

    mp_of = relationship("Offices")
