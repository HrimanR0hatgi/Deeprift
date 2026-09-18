from fastapi import APIRouter, HTTPException

from models.schemas import SimulationRequest
from simulation.engine import run_simulation


router = APIRouter()


@router.post("/simulate")
def simulate(data: SimulationRequest):

    try:
        return run_simulation(data)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )