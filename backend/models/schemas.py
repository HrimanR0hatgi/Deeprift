from typing import Literal, Union
from pydantic import BaseModel, Field


class EarthquakeRequest(BaseModel):
    disaster: Literal["earthquake"]
    latitude: float
    longitude: float
    magnitude: float = Field(ge=0, le=10)
    depth_km: float = Field(ge=0)


class FloodRequest(BaseModel):
    disaster: Literal["flood"]
    latitude: float
    longitude: float
    water_depth_m: float = Field(ge=0)
    rainfall_mm: float = Field(ge=0)


class CycloneRequest(BaseModel):
    disaster: Literal["cyclone"]
    latitude: float
    longitude: float
    wind_speed_kmh: float = Field(ge=0)
    rainfall_mm: float = Field(ge=0)
    storm_surge_m: float = Field(ge=0)


class WildfireRequest(BaseModel):
    disaster: Literal["wildfire"]
    latitude: float
    longitude: float
    spread_rate_kmh: float = Field(ge=0)
    temperature_c: float
    wind_speed_kmh: float = Field(ge=0)
    humidity_percent: float = Field(ge=0, le=100)


SimulationRequest = Union[
    EarthquakeRequest,
    FloodRequest,
    CycloneRequest,
    WildfireRequest
]