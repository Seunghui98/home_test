import requests
import time
import base64

payload = {
    "ServiceName": "pose_detection",
    "ServiceInfo": [
    {
        "ExecutionType": "container",
    }] 
}
start = time.time()
with open('emergency.png', 'rb') as f:
    im_b64 = base64.b64encode(f.read()).decode('utf8')


headers = {}
url = 'http://localhost:56001/api/v1/orchestration/services'

r = requests.post(url, json=payload, headers=headers)

if r.ok:
    result = r.json()
    print(result)
    ip = result['RemoteTargetInfo']['Target']
    print(ip)
    imagejson = {'img_base64':im_b64}
    headers = {}
    url = 'http://'+ip+':3500/pose_detection'

    r2 = requests.post(url, json=imagejson, headers=headers)

    if r2.ok:
        pose = r2.json()
        print(pose)
        print("time :", time.time() - start)
    
    
    
 
