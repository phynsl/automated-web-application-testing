import requests

def test_login_load():
    user = {"email": "admin@example.com", "password": "wrongpass"}
    for _ in range(100):
        r = requests.post("http://localhost/selfconcept/login.php", data=user)
        assert "Invalid" in r.text
