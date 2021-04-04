import requests

with open("table1.xlsx", "rb") as f:
    requests.post("http://127.0.0.1:5000/users", f)
