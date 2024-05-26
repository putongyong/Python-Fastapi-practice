from sqlalchemy import Column, Integer, String, Float, Date, Enum as SQLAlchemyEnum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class GroupType(enum.Enum):
    group1 = "group1"
    group2 = "group2"
    group3 = "group3"

class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    installation_date = Column(Date)
    max_power_megawatt = Column(Float)
    min_power_megawatt = Column(Float)
    useful_energy_at_1_megawatt = Column(Float)


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(SQLAlchemyEnum(GroupType))
