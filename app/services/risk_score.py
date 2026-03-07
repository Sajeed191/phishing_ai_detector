def calculate_risk(features, keywords, ml_prediction):

    score = 0

    if features["url_length"] > 75:
        score += 20

    if features["https"] == 0:
        score += 15

    if features["ip_in_url"]:
        score += 20

    if features["subdomain_count"] > 3:
        score += 15

    if len(keywords) > 0:
        score += 10

    if ml_prediction == 1:
        score += 20

    return min(score, 100)