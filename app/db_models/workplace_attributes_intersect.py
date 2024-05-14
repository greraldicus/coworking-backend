from app.db import Base

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class WorkplaceAttributesIntersect(Base):
    __tablename__ = "WorkplaceAttributesIntersect"

    wptypeattr_wp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    wptypeattr_wp_wptypeattr_id = Column(Integer, ForeignKey('WorkplaceTypeAttributes.wptypeattr_id'), nullable=False)
    wptypeattr_wp_wp_id = Column(Integer, ForeignKey('Workplaces.wp_id'), nullable=False)

    wptypeattr_wp_wp = relationship('Workplaces')
    wptypeattr_wp_wptypeattr = relationship('WorkplaceTypeAttributes')
