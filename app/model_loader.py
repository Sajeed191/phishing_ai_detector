import joblib

def get_model():
    model = joblib.load("model/phishing_model.pkl")
    return model
