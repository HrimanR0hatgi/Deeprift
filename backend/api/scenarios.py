import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.database import get_db
from models.models import Scenario


router = APIRouter(prefix="/api/scenarios", tags=["Scenarios"])


@router.post("")
def save_scenario(
    name: str,
    disaster: str,
    latitude: float,
    longitude: float,
    input_parameters: dict,
    simulation_result: dict,
    user_id: int,
    db: Session = Depends(get_db)
):
    scenario = Scenario(
        user_id=user_id,
        name=name,
        disaster=disaster,
        latitude=latitude,
        longitude=longitude,
        input_parameters=json.dumps(input_parameters),
        simulation_result=json.dumps(simulation_result)
    )

    db.add(scenario)
    db.commit()
    db.refresh(scenario)

    return {
        "message": "Scenario saved successfully",
        "scenario_id": scenario.id
    }


@router.get("")
def get_scenarios(
    user_id: int,
    db: Session = Depends(get_db)
):
    scenarios = (
        db.query(Scenario)
        .filter(Scenario.user_id == user_id)
        .order_by(Scenario.created_at.desc())
        .all()
    )

    return [
        {
            "id": scenario.id,
            "name": scenario.name,
            "disaster": scenario.disaster,
            "latitude": scenario.latitude,
            "longitude": scenario.longitude,
            "input_parameters": json.loads(scenario.input_parameters),
            "simulation_result": json.loads(scenario.simulation_result),
            "created_at": scenario.created_at
        }
        for scenario in scenarios
    ]


@router.get("/{scenario_id}")
def get_scenario(
    scenario_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    scenario = (
        db.query(Scenario)
        .filter(
            Scenario.id == scenario_id,
            Scenario.user_id == user_id
        )
        .first()
    )

    if not scenario:
        raise HTTPException(
            status_code=404,
            detail="Scenario not found"
        )

    return {
        "id": scenario.id,
        "name": scenario.name,
        "disaster": scenario.disaster,
        "latitude": scenario.latitude,
        "longitude": scenario.longitude,
        "input_parameters": json.loads(scenario.input_parameters),
        "simulation_result": json.loads(scenario.simulation_result),
        "created_at": scenario.created_at
    }
@router.delete("/{scenario_id}")
def delete_scenario(
    scenario_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    scenario = (
        db.query(Scenario)
        .filter(
            Scenario.id == scenario_id,
            Scenario.user_id == user_id
        )
        .first()
    )

    if not scenario:
        raise HTTPException(
            status_code=404,
            detail="Scenario not found"
        )

    db.delete(scenario)
    db.commit()

    return {
        "message": "Scenario deleted successfully"
    }