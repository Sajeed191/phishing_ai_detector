from app.model_loader import load_model
import numpy as np

model = load_model()

def predict(features):

    feature_vector = np.array([
        features["url_length"],
        features["https"],
        features["subdomain_count"],
        features["ip_in_url"],
        features["special_chars"]
    ]).reshape(1,-1)

    prediction = model.predict(feature_vector)

    return int(prediction[0])