import joblib

def load_model():

    model = joblib.load("model/phishing_model.pkl")

    return model