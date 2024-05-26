# schemas.py
from pydantic import BaseModel
from datetime import date
from enum import Enum

class GroupType(str, Enum):
    group1 = "group1"
    group2 = "group2"
    group3 = "group3"

class SiteCreate(BaseModel):
    name: str
    installation_date: date
    max_power_megawatt: float
    min_power_megawatt: float
    useful_energy_at_1_megawatt: float

class GroupCreate(BaseModel):
    name: str
    type: GroupType

class ResponseSite(BaseModel):
    id: int
    name: str
    installation_date: date
    max_power_megawatt: float
    min_power_megawatt: float
    useful_energy_at_1_megawatt: float

class ResponseGroup(BaseModel):
    id: int
    name: str
    type: GroupType
