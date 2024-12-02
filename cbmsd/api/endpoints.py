from cbmsd.api import app
from cbmsd import save_mapset, mirrors
import os
import json

@app.get("/d/{id}")
async def download_mapset(id: str):
    with open("settings.json") as f:
        cfg = json.load(f)
    filename = save_mapset(id, cfg["mirror"])["Filename"]
    os.startfile(filename)
    return {"Success": "Mapset saved"}

@app.get("/api/settings")
async def get_settings():
    with open("settings.json") as f:
        return json.load(f)

@app.post("/api/settings")
async def set_settings(settings: dict):
    if settings["mirror"] not in mirrors:
        return {"Error": "Invalid mirror selected"}
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)
    return {"Success": "Settings saved"}

@app.options("/api/settings")
async def set_settings():
    return "OK."
