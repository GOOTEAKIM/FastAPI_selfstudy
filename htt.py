import httpx

r = httpx.get("http://localhost:8000/hi")
r.json()