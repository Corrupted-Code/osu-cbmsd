from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8081",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8081",
    "https://osu.ppy.sh"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from cbmsd.api.endpoints import *
