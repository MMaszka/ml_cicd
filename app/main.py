from fastapi import FastAPI
from app.model import load_model, predict
from app.ai_integration import analyze_text

app = FastAPI()

model = load_model()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/predict")
def predict_endpoint(data: dict):
    return predict(model, data)

@app.post("/ai")
def ai_endpoint(text: str):
    return analyze_text(text)
