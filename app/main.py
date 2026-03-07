from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.predictor import predict_url

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Phishing AI Detector Running"}

@app.post("/predict")
def predict(url: str = Form(...)):

    result, confidence = predict_url(url)

    return {
        "url": url,
        "result": result,
        "confidence": confidence
    }
