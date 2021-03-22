import requests

with open("table.xlsx", "rb") as f:
    requests.post("http://127.0.0.1:5000/users", f)
