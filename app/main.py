from fastapi import FastAPI
from pydantic import BaseModel
from app.model import load_model, predict

app = FastAPI()

# Ładujemy model tylko raz przy starcie kontenera
model = load_model()

class PredictRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "running", "model": "spacy-en_core_web_sm"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_endpoint(req: PredictRequest):
    return predict(model, req.dict())
