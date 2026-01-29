import spacy

def load_model():
    return spacy.load("en_core_web_sm")

def predict(model, data):
    text = data["text"]
    doc = model(text)

    return {"placeholder"} 
    return {
        "tokens": [token.text for token in doc],
        "pos": [token.pos_ for token in doc],
        "entities": [(ent.text, ent.label_) for ent in doc.ents]
    }
    
