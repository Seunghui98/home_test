import requests
import time

payload = {
    "ServiceName": "hello-world",
    "ServiceInfo": [
    {
        "ExecutionType": "container",
        "ExecCmd": [
            "docker",
            "run",
            "-v", "/var/run:/var/run:rw",
            "hello-world"
        ]
    }],
    "StatusCallbackURI": "http://localhost:8888/api/v1/services/notification"
}

headers = {}
url = 'http://localhost:56001/api/v1/orchestration/services'

r = requests.post(url, json=payload, headers=headers)

if r.ok:
    result = r.json()
    print(result)
    url2 = result['RemoteTargetInfo']['Target']
    print(url2)
    respose = requests.get("http://"+url2+":3333/ping")
    print(respose.json())
