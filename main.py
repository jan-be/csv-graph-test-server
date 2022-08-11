"""
this is the new server backend running with fastAPI
to run type (at root), you might want to add --reload for debugging:
uvicorn scripts.server.webserver_backend:app --host 0.0.0.0
"""
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def entrypage():
    return {"message": "Hello World", "documentation": "/docs"}


@app.get("/graphs/{graphId}/root")
async def get_root(graphId: int):
    with open('outputfile.json') as f:
        d = json.load(f)

    return {"graph": d}
