import threading
print("Starting Osu!CBMSD...")
def run_fastapi():
    from cbmsd.api import app as fastapi_app

    import uvicorn
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8081, log_config=None)


threading.Thread(target=run_fastapi).start()
print("API running at: http://localhost:8081")
print("Started Osu!CBMSD.")

