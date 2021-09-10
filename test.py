import requests

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
