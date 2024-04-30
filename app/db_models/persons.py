from app.db import Base

from sqlalchemy import Column, TEXT, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Persons(Base):
    __tablename__ = "Persons"

    prsn_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    prsn_name = Column(TEXT, nullable=False)
    prsn_surname = Column(TEXT, nullable=False)
    prsn_patronymic = Column(TEXT)
    prsn_tenr_id = Column(Integer, ForeignKey('Tenures.tenr_id'), nullable=False)

    prsn_tenr = relationship('Tenures')
