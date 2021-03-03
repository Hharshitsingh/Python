import requests
import datetime as dt
GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 169
AGE = 21
APP_ID = ""
APP_KEY = ""
SHEETY_AUTH = ""
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_endpoint = ""
exercise_text = input("which exercise you did: ")
exercise_headers = {
    "x-app-id" : APP_ID,
    "x-app-key" :APP_KEY
}
exercise_params = {
    "query": exercise_text,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}
sheets_headers = {
    "Authorization": SHEETY_AUTH
}

response = requests.post(exercise_endpoint, json=exercise_params, headers = exercise_headers)
response.raise_for_status()
data = response.json()
print()
for exercise in data["exercises"] :
    today_date = dt.datetime.now().strftime("%d/%m/%Y")
    now_time = dt.datetime.now().strftime("%X")
    sheet_input = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }
    }

    sheet_response = requests.post(url=sheets_endpoint, json= sheet_input, headers = sheets_headers )
    print(sheet_response.text)
