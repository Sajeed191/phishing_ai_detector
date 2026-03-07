def analyze_url(url):

    threats = []

    if len(url) > 75:
        threats.append("URL too long")

    if "@" in url:
        threats.append("Contains @ symbol")

    if url.count('.') > 5:
        threats.append("Too many subdomains")

    if "-" in url:
        threats.append("Hyphen detected")

    return threats