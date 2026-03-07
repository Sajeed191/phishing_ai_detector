import re
from urllib.parse import urlparse

def extract_features(url):

    features = []

    parsed = urlparse(url)

    domain = parsed.netloc
    path = parsed.path

    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(url.count('@'))
    features.append(url.count('?'))
    features.append(url.count('%'))
    features.append(url.count('='))
    features.append(len(domain))
    features.append(len(path))

    suspicious_words = ["login","secure","account","update","bank","verify"]

    score = 0

    for word in suspicious_words:
        if word in url.lower():
            score += 1

    features.append(score)

    return features