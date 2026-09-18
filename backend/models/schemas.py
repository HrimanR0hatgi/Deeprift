from pydantic import BaseModel


class SimulationRequest(BaseModel):
    disaster: str
    latitude: float
    longitude: float
    intensity: float