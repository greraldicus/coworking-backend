from app.db import Base

from sqlalchemy import Column, TEXT, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = "Users"

    usr_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    usr_prsn_id = Column(Integer, ForeignKey('Persons.prsn_id'), nullable=False)
    usr_rol_id = Column(Integer, ForeignKey('Roles.rol_id'), nullable=False)
    usr_login = Column(TEXT, nullable=False, unique=True)
    usr_hashed_password = Column(TEXT, nullable=False)

    usr_prsn = relationship('Persons')
    usr_rol = relationship('Roles')
