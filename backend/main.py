from fastapi import FastAPI

from api.simulation import router as simulation_router
from api.auth import router as auth_router
from api.scenarios import router as scenarios_router

app = FastAPI(title="DeepRift API")

app.include_router(simulation_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(scenarios_router)

@app.get("/")
def root():
    return {"message": "DeepRift backend is running"}