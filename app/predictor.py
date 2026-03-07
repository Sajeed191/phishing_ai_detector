from app.feature_extractor import extract_features
from app.model_loader import get_model

def predict_url(url):

    model = get_model()

    features = extract_features(url)

    prediction = model.predict([features])[0]

    probability = model.predict_proba([features])[0][1]

    return prediction, probability