import requests
question_data = []
response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
response.raise_for_status()
data = response.json()
question_data = data["results"]
print(question_data)
