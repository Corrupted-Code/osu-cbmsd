import requests
import os
from win10toast import ToastNotifier
toast = ToastNotifier()

#Mino mirror is recommended.

def save_mapset(id, mirror="https://catboy.best/d/"):
    send_notification("Osu!CBMSD", "Downloading mapset...")
    
    try:
        response = requests.get(mirror + id, stream=True)
        response.raise_for_status()  # Raises HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        send_notification("Osu!CBMSD", f"Failed to download mapset: {e}")
        return {"Error": f"Failed to download mapset: {e}"}
    
    content_disposition = response.headers.get('Content-Disposition')
    if not content_disposition:
        send_notification("Osu!CBMSD", "Filename not found in headers.")
        return {"Error": "Filename not found in headers."}
    
    filename = content_disposition.split('filename=')[-1].strip('"').replace('%20', ' ')
    
    try:
        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    except IOError as e:
        send_notification("Osu!CBMSD", f"Failed to save mapset: {e}")
        return {"Error": f"Failed to save mapset: {e}"}
    
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
