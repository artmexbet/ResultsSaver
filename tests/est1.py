import requests

data = requests.post("http://127.0.0.1:5000/add_result/7019", json={"subject": "История", "score": 30})
print(data.json())
# data = requests.put("http://127.0.0.1:5000/change_day", json={"new_day": 1})
