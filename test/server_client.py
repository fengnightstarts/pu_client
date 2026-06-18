import requests
from datetime import datetime

login_url = "http://localhost:8080/login"
join_url = "http://localhost:8080/join"
status_url = "http://localhost:8080/status"
user = {"userName": "admin", "password": None, "sid": 111111, "token": "admin"}
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(current_time)
act1 = {
    "sid": 111111,
    "userName": "admin",
    "activity": {
        "id": "123123123123",
        "name": "test1",
        "joinStartTime": "2025-02-27 22:44:02",
        "joinEndTime": "2025-02-27 23:44:02",
    },
}

act2 = {
    "sid": 111111,
    "userName": "admin",
    "activity": {
        "id": "234234234234",
        "name": "test2",
        "joinStartTime": "2025-03-01 10:00:00",
        "joinEndTime": "2025-03-01 11:00:00",
    },
}

act3 = {
    "sid": 111111,
    "userName": "admin",
    "activity": {
        "id": "345345345345",
        "name": "test3",
        "joinStartTime": "2025-04-15 14:30:00",
        "joinEndTime": "2025-04-15 15:30:00",
    },
}
acts = [act1, act2, act3]
# print(user)
response = requests.post(login_url, json=user)
print(response.text)
for act in acts:
    response = requests.post(join_url, json=act)
    print(response.text)
response = requests.post(status_url, json=user)
print(response.text)
