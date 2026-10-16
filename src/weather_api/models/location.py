from typing import Annotated
from pydantic import BaseModel, Field


class LocationQuery(BaseModel):
    name: Annotated[str, Field(min_length=2)]
    language: str = "english"


class Location(BaseModel):
    name: str
    country: str
    latitude: float
    longitude: float
    timezone: str