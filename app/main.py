from fastapi import FastAPI
from pydantic import BaseModel

from app.services.url_analyzer import analyze_url
from app.services.keyword_detector import detect_keywords
from app.services.risk_scorer import calculate_risk
from app.predictor import predict
from app.utils.validators import is_valid_url

app = FastAPI()

class URLRequest(BaseModel):
    url: str


@app.post("/analyze")
def analyze(request: URLRequest):

    url = request.url

    if not is_valid_url(url):
        return {"error": "Invalid URL"}

    features = analyze_url(url)

    keywords = detect_keywords(url)

    ml_prediction = predict(features)

    risk_score = calculate_risk(features, keywords, ml_prediction)

    return {
        "url": url,
        "risk_score": risk_score,
        "keywords_found": keywords,
        "features": features,
        "ml_prediction": ml_prediction
    }
