from app.db import Base

from sqlalchemy import Column, TEXT, Integer, ForeignKey
from sqlalchemy.orm import relationship


class WorkplaceAttributes(Base):
    __tablename__ = "WorkplaceAttributes"

    wpattr_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    wpattr_value = Column(TEXT, nullable=False, unique=True)
    wpattr_attr_id = Column(Integer, ForeignKey('Attributes.attr_id'), nullable=False)

    wpattr_attr = relationship('Attributes')
