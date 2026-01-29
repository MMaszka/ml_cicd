from transformers import pipeline

def load_model():
    # Ładuje gotowy model HuggingFace
    return pipeline("sentiment-analysis")

def predict(model, data):
    text = data["text"]
    result = model(text)[0]
    return {
        "label": result["label"],
        "score": float(result["score"])
    }
