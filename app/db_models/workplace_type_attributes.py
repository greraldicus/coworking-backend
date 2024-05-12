from app.db import Base

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class WorkplaceTypeAttributes(Base):
    __tablename__ = "WorkplaceTypeAttributes"

    wptypeattr_wpattr_id = Column(Integer, ForeignKey('WorkplaceAttributes.wpattr_attr_id'), nullable=False)
    wptypeattr_wptype_id = Column(Integer, ForeignKey('WorkplaceTypes.wptype_id'), nullable=False)
    wptypeattr_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    wptypeattr_wpattr = relationship('WorkplaceAttributes')
    wptypeattr_wptype = relationship('WorkplaceTypes')
