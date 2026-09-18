from fastapi import APIRouter

from models.schemas import SimulationRequest

from simulation.engine import run_simulation

router = APIRouter()


@router.post("/simulate")
def simulate(request: SimulationRequest):
    return run_simulation(
        request.disaster,
        request.latitude,
        request.longitude,
        request.intensity
    )