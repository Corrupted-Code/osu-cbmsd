from cbmsd import save_mapset
import os
import time

start_time = time.time()

from cbmsd.api import app
from fastapi.responses import HTMLResponse

@app.get("/d/{id}")
async def download_mapset(id: str):
    try:
        result = save_mapset(id, "https://catboy.best/d/")
        if "Error" in result:
            return {"Error": result["Error"]}
        
        filename = result.get("Filename")
        if not filename:
            return {"Error": "Filename not found after downloading mapset."}

        try:
            os.startfile(filename)
        except Exception as e:
            return {"Error": f"Failed to open file: {e}"}

        try:
            with open("cbmsd/htmls/downloaded.html") as f:
                html = f.read()
        except FileNotFoundError:
            return {"Error": "HTML file for response not found."}
        except Exception as e:
            return {"Error": f"Failed to read HTML file: {e}"}

        return HTMLResponse(content=html, status_code=200)
    except Exception as e:
        return {"Error": str(e)}

@app.get("/api/status")
async def set_settings():
    uptime = int(time.time() - start_time)
    return {"status": "online", "uptime": uptime}



