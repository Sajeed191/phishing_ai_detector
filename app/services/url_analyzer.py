from urllib.parse import urlparse
import re

def analyze_url(url):

    parsed = urlparse(url)

    features = {}

    features["url_length"] = len(url)

    features["https"] = 1 if parsed.scheme == "https" else 0

    features["subdomain_count"] = parsed.netloc.count(".")

    ip_pattern = r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"

    features["ip_in_url"] = 1 if re.search(ip_pattern, url) else 0

    features["special_chars"] = url.count("@") + url.count("-")

    return features