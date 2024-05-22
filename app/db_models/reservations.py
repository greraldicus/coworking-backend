from app.db import Base

from sqlalchemy import Column, TEXT, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Reservations(Base):
    __tablename__ = "Reservations"

    res_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    res_wp_id = Column(Integer, ForeignKey("Workplaces.wp_id"), nullable=False)
    res_start_time = Column(TEXT, nullable=False)
    res_end_time = Column(TEXT, nullable=False)
    res_date = Column(TEXT, nullable=False)
    res_of_prsn_id = Column(Integer, ForeignKey("OfficePersonIntersect.of_prsn_id"))

    res_wp = relationship('Workplaces')
    res_of_prsn = relationship('OfficePersonIntersect')
