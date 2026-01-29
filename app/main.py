from transformers import pipeline

def load_model():
    return pipeline("sentiment-analysis", framework="tf")


def predict(model, data):
    text = data["text"]
    result = model(text)[0]
    return {
        "label": result["label"],
        "score": float(result["score"])
    }
