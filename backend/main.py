from fastapi import FastAPI
from api.simulation import router as simulation_router

app = FastAPI(title="DeepRift API")

app.include_router(simulation_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "DeepRift backend is running"}