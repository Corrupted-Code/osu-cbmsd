import json
import os
import threading
import eel

default_settings = {
    "mirror": "catboybest",
}

settings_file = "settings.json"
if not os.path.exists(settings_file):
    with open(settings_file, "w") as f:
        json.dump(default_settings, f, indent=4)

with open(settings_file) as f:
    settings = json.load(f)


def run_fastapi():
    from cbmsd.api import app as fastapi_app

    import uvicorn
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8081)


threading.Thread(target=run_fastapi).start()

eel.init('cbmsd/interface')
eel.start('index.html', size=(800, 600))

