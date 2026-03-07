from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.predictor import predict_url
from app.services.url_analyzer import analyze_url
from app.utils.validators import is_valid_url

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

@app.post("/predict")
def predict(data: URLRequest):

    url = data.url

    if not is_valid_url(url):
        return {"error":"Invalid URL"}

    prediction = predict_url(url)

    threats = analyze_url(url)

    prediction["threat_indicators"] = threats

    return prediction