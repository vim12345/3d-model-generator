from fastapi import FastAPI
from fastapi.responses import FileResponse
import subprocess
import uuid
import os

app = FastAPI()

@app.get("/status")
def get_status():
    return {"status": "ready", "model": "Shap-E"}

@app.get("/generate3d")
def generate_3d(prompt: str):
    uid = uuid.uuid4().hex[:6]
    filename = f"{prompt.replace(' ', '_')}_{uid}.glb"
    full_path = os.path.join("outputs", filename)

    # Run generation script with prompt
    command = f"python generate.py \"{prompt}\""
    subprocess.run(command, shell=True)

    # Find the newest .glb file in outputs
    files = sorted(os.listdir("outputs"), key=lambda x: os.path.getmtime(os.path.join("outputs", x)))
    latest_file = files[-1] if files else None

    return {"prompt": prompt, "generated_file": latest_file}

@app.get("/download")
def download_file(file: str):
    return FileResponse(f"outputs/{file}")
