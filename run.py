import requests

requests.post(url="http://127.0.0.1:1234/", json={"msg": "hello1"})
r = requests.get(url="http://127.0.0.1:1234/")
print(r.text)

requests.post(url="http://127.0.0.1:1234/", json={"msg": "hello2"})
r = requests.get(url="http://127.0.0.1:1234/")
print(r.text)

requests.post(url="http://127.0.0.1:1234/", json={"msg": "hello3"})
r = requests.get(url="http://127.0.0.1:1234/")
print(r.text)