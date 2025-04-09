 
# ✅ 1. Clone and Set Up

git clone https://github.com/your-username/3d-model-generator.git

cd 3d-model-generator
# ✅ 2. Install Requirements

pip install -r requirements.txt
# ✅ 3. Install Shap-E

git clone https://github.com/openai/shap-e.git

cd shap-e

pip install -e .

cd ..
# ✅ 4. Run the FastAPI Server

uvicorn api.main:app --reload

# 📡 API Endpoints
# 🔍 GET /status
Check if the model is ready.


curl http://127.0.0.1:8000/status
# Response:

json

{"status": "ready", "model": "Shap-E"}
🧠 GET /generate3d?prompt=...
Generate a 3D model from a text prompt.


curl "http://127.0.0.1:8000/generate3d?prompt=a flying dragon"
# Response:

json

{
  "prompt": "a flying dragon",
  "generated_file": "a_flying_dragon_bf23d4.glb"
}
# 💾 GET /download?file=...
Download the generated .glb file.


curl -O "http://127.0.0.1:8000/download?file=a_flying_dragon_bf23d4.glb"
# 📁 Output Directory
All generated files are saved in the outputs/ folder:

outputs/
├── a_flying_dragon_bf23d4.glb


# 🧪 Demo Output
You can preview .glb files using:

# 🌐 https://gltf-viewer.donmccurdy.com

📦 Project Structure
bash
Copy code
3d-model-generator/
├── api/
│   └── main.py            # FastAPI server
├── shap-e/                # Shap-E cloned repo
├── outputs/               # Generated .glb files
├── generate.py            # Script to run text-to-3D
├── requirements.txt
├── README.md