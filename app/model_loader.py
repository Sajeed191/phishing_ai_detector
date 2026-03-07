import joblib

model = joblib.load("model/phishing_model.pkl")

def get_model():
    return model