import socket 

def test_dns_resolution():
    hostname = "example.com"
    ip = socket.gethostbyname(hostname)
    assert ip.startswith("93.") # IP from 93 subnet  
