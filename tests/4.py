import requests

data1 = requests.post("http://127.0.0.1:5000/add_admin",
                      json={"login": "aa", "password": "a", "name": "Артём", "subject": "Memology11",
                            "is_admin": True})
print(data1.content)
data = requests.post("http://127.0.0.1:5000/check_admins", json={"login": "artmebet", "password": "assas"})
print(data.json())
