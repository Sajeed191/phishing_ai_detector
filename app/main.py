from flask import Flask, request, jsonify
from app.services.url_analyzer import analyze_url
from app.services.keyword_detector import detect_keywords
from app.services.risk_scorer import calculate_risk
from app.predictor import predict
from app.utils.validators import is_valid_url

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])

def analyze():

    data = request.json

    url = data.get("url")

    if not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    features = analyze_url(url)

    keywords = detect_keywords(url)

    ml_prediction = predict(features)

    risk_score = calculate_risk(features, keywords, ml_prediction)

    return jsonify({

        "url": url,
        "risk_score": risk_score,
        "keywords_found": keywords,
        "features": features,
        "ml_prediction": ml_prediction

    })

if __name__ == "__main__":
    app.run(debug=True)