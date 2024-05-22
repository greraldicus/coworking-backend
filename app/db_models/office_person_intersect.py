from app.db import Base

from sqlalchemy import Column, TEXT, Integer, ForeignKey
from sqlalchemy.orm import relationship


class OfficePersonIntersect(Base):
    __tablename__ = "OfficePersonIntersect"

    of_prsn_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    of_prsn_prsn_id = Column(Integer, ForeignKey("Persons.prsn_id"), nullable=False)
    of_prsn_of_id = Column(Integer, ForeignKey("Offices.of_id"), nullable=False)

    of_prsn_prsn = relationship('Persons')
    of_prsn_of = relationship('Offices')
