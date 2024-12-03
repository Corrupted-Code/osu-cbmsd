from cbmsd import save_mapset
import os
import time

start_time = time.time()

from cbmsd.api import app
from fastapi.responses import HTMLResponse

@app.get("/d/{id}")
async def download_mapset(id: str):
    try:
        filename = save_mapset(id, "https://catboy.best/d/")["Filename"]
        os.startfile(filename)
        with open("cbmsd/htmls/downloaded.html") as f:
            html = f.read()
        return HTMLResponse(content=html, status_code=200)
    except Exception as e:
        return {"Error": str(e)}

@app.get("/api/status")
async def set_settings():
    uptime = int(time.time() - start_time)
    return {"status": "online", "uptime": uptime}


