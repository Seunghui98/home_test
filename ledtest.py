import requests

payload1 = {'emotion': 'DISGUST'}
payload2 = {'pose': 'clap'}
headers = {}
url1 = 'http://localhost:4000/emotion'
url2 = 'http://localhost:4000/pose'

r = requests.post(url1, json=payload1, headers=headers)
#r2 = requests.post(url2, json=payload2, headers=headers)
