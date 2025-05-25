from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from external JSON file
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

# Convert to dictionary for faster lookup
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
def get_marks(name: List[str] = []):
    results = [marks_dict.get(n, None) for n in name]
    return {"marks": results}
