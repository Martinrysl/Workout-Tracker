import requests
from datetime import datetime

APP_ID = ""
APP_KEY = ""

exercise_in = input("Tell me which exercise you did: ")
track_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/931775cd4d444ee725ce2a08b6b77555/copiaDeMyWorkouts/workouts"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_params = {
    "query": exercise_in,
    "gender": "male",
    "weight_kg": 82,
    "height_cm": 175,
    "age": 22,
}
response = requests.post(track_endpoint, json=exercise_params, headers=headers)
result = response.json()
print(result)

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)
