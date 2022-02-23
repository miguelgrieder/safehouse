import time
import requests

while True:
    request_addStatus = requests.post('http://127.0.0.1:8000/addStatus')
    print(request_addStatus.json())
    time.sleep(30)
