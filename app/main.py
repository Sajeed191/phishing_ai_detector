from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from app.predictor import predict_url

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Phishing AI Detector API"}

@app.post("/predict")
def detect(url: str = Form(...)):

    prediction, probability = predict_url(url)

    result = "Phishing" if prediction == 1 else "Legitimate"

    return {
        "url": url,
        "result": result,
        "confidence": float(probability)
    }