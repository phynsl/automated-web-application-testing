import requests

BASE_URL = "https://example.com"
paths = [
    "/", "/login", "/admin", "/api/health", "/api/status", "/dashboard", "/nonexistent"
]

for path in paths:
    url = BASE_URL + path
    try:
        response = requests.get(url, timeout=5)
        print(f"{url} → {response.status_code}")
    except requests.RequestException as e:
        print(f"{url} → Error: {e}")
