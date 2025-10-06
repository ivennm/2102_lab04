import httpx

BASE_URL = "http://localhost:5000/"

# Test GET request
response = httpx.get(BASE_URL)
print("GET /:", response.status_code, response.text)

# Test POST request
mydata = {"text": "Hello from client!"}
response = httpx.post(BASE_URL + "echo", data=mydata)
print("POST /echo:", response.status_code, response.text)

# Test factoring endpoint
for n in [12, 13, 360]:
    r = httpx.get(BASE_URL + f"factors?inINT={n}")
    print(f"GET /factors?inINT={n}:", r.status_code, r.text)
