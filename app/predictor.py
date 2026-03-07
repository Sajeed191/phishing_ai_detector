from app.feature_extractor import extract_features
from app.model_loader import get_model

model = get_model()

def predict_url(url):

    features = extract_features(url)

    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0][1]

    if prediction == 1:
        result = "Phishing"
    else:
        result = "Safe"

    return result, float(probability)
