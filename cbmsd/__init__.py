import requests
import os
from win10toast import ToastNotifier
toast = ToastNotifier()

#catboy.best mirror is recommended.

mirrors = ["https://beatconnect.io/b/", "https://catboy.best/d/", "https://osu.direct/d/"]

def save_mapset(id, mirror = "https://catboy.best/d/"):
    send_notification("Osu!CBMSD", "Downloading mapset...")
    response = requests.get(mirror + id, stream=True)
    if response.status_code != 200:
        send_notification("Osu!CBMSD", "Failed to download mapset.")
        return {"Error": "Failed to download mapset."}
    filename = response.headers.get('Content-Disposition').split('filename=')[-1].strip('"')
    with open(filename, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    send_notification("Osu!CBMSD", "Mapset downloaded.")
    return {"Success": "Mapset saved as", "Filename": filename}

def send_notification(title, body, icon_path = None, duration = 5, threaded = True):
    toast.show_toast(
        title,
        body,
        icon_path = icon_path,
        duration=duration,
        threaded = threaded,
    )
