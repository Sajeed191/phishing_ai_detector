import re
from urllib.parse import urlparse

def extract_features(url):

    parsed = urlparse(url)

    features = {}

    features['url_length'] = len(url)
    features['domain_length'] = len(parsed.netloc)
    features['has_https'] = 1 if parsed.scheme == "https" else 0
    features['count_dots'] = url.count(".")
    features['count_hyphen'] = url.count("-")
    features['count_at'] = url.count("@")
    features['count_question'] = url.count("?")
    features['count_percent'] = url.count("%")
    features['count_equal'] = url.count("=")

    suspicious_words = ["login","secure","update","bank","verify","account"]

    features['suspicious_words'] = sum(word in url.lower() for word in suspicious_words)

    return list(features.values())