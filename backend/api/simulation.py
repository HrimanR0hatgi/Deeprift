from fastapi import APIRouter, HTTPException

from models.schemas import SimulationRequest
from simulation.engine import run_simulation
from osm_data import get_nearby_services


router = APIRouter()


@router.post("/simulate")
def simulate(data: SimulationRequest):

    try:
        simulation_result = run_simulation(data)

        osm_result = get_nearby_services(
            data.latitude,
            data.longitude,
            simulation_result["affected_radius_km"]
        )

        return {
            **simulation_result,
            **osm_result
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
