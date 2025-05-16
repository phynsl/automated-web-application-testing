import requests

def test_status_code_ok():
    response = requests.get("https://example.com/api/health")
    assert response.status_code == 200

def test_status_code_not_found():
    response = requests.get("https://example.com/api/nonexistent")
    assert response.status_code == 404
