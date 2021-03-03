import requests
from requests.api import patch
from datetime import datetime
USERNAME = ""
TOKEN = ""
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# respone = requests.post(url=pixela_endpoint, json=user_params)
# print(respone.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "coding",
    "unit": "hours",
    "type": "float",
    "color": "kuro"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

today = datetime.now()
pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6.5",
}
print(pixel_data)
pixel_response = requests.post(url=pixel_creation, json=pixel_data, headers= headers)
print(pixel_response.text)