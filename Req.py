import requests

r = requests.get("http://localhost:8000/hi")
r.json()

params = {"who":"Mom"}

r = requests.post("http://localhost:8000/hi", params=params)

r.json()
