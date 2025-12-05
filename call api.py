import requests

res = requests.get("http://127.0.0.1:8000/read")
print(res.json())

update = {
    "data": {
        "test": "hello",
        "value": 42
    }
}

res = requests.post("http://127.0.0.1:8000/update", json=update)
print(res.json())
