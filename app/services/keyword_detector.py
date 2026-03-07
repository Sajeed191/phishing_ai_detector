SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "bank",
    "account",
    "secure",
    "update",
    "password",
    "signin",
    "confirm",
    "ebay",
    "paypal"
]

def detect_keywords(url):

    found = []

    for word in SUSPICIOUS_KEYWORDS:
        if word in url.lower():
            found.append(word)

    return found