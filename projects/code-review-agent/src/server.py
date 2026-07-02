from fastapi import FastAPI, Depends
from .config import Settings, get_settings


app = FastAPI()

@app.get("/config")
def current_settings(settings: Settings=Depends(get_settings)):
    return {"api_key": settings.api_key[:3], "model": settings.model}
    