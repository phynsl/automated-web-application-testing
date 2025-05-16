import time 
from urllib import request

host = "http://172.19.79.102:8000/"
opener = request.build_opener()
request = request.Request(host)
request.add_header('user-agent', 'firefox')
start = time.time()
resp = opener.open(request)

resp.read(1)
ttfb = time.time() - start

print("The time to get first byte of " +host+" is: "+str(ttfb) + " milliseconds")


