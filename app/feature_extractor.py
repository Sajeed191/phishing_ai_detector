from urllib.parse import urlparse

def extract_features(url):

    parsed = urlparse(url)

    features = []

    features.append(len(url))
    features.append(len(parsed.netloc))
    features.append(url.count("."))
    features.append(url.count("-"))
    features.append(url.count("@"))
    features.append(url.count("?"))
    features.append(url.count("%"))
    features.append(url.count("="))

    if "https" in url:
        features.append(1)
    else:
        features.append(0)

    suspicious_words = ["login","verify","bank","secure","update","account"]

    count = 0
    for word in suspicious_words:
        if word in url.lower():
            count += 1

    features.append(count)

    return features
