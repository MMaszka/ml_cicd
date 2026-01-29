from fastapi import FastAPI
from pydantic import BaseModel
from app.model import load_model, predict
from app.ai_integration import analyze_text

app = FastAPI()

# Ładowanie modelu przy starcie aplikacji
model = load_model()

# Schemat danych wejściowych
class PredictRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/predict")
def predict_endpoint(req: PredictRequest):
    # Zamieniamy dane na dict i przekazujemy do modelu
    return predict(model, req.dict())


@app.post("/ai")
def ai_endpoint(text: str):
    return analyze_text(text)
