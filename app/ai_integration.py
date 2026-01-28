import os
import requests

AI_ENDPOINT = os.getenv("AI_ENDPOINT")
AI_KEY = os.getenv("AI_KEY")

def analyze_text(text: str):
    headers = {
        "Ocp-Apim-Subscription-Key": AI_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "documents": [
            {"id": "1", "language": "en", "text": text}
        ]
    }

    response = requests.post(
        f"{AI_ENDPOINT}/text/analytics/v3.1/sentiment",
        headers=headers,
        json=payload
    )

    return response.json()

