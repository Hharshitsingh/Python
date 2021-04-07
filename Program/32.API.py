import requests
reponse = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(reponse.status_code)
reponse.raise_for_status()
data = reponse.json()
print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
tup = (latitude,longitude)
print(tup)

