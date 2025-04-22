import requests
from datetime import datetime
Application_id="f2ed9343"
Api_Key="2341eb90af6e72b92f68ba532a70261f"
header={
    "x-app-id":Application_id,
    "x-app-key":Api_Key,
}
exercise_text = input("Tell me which exercises you did: ")
parameters={
    "query":exercise_text,
    "gender": "Male",
    "weight_kg": "93",
    "height_cm":"10.93",
    "age": "19"

}
wensite="https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=wensite,json=parameters,headers=header)
response1 = response.json()
print(response1)
website="https://api.sheety.co/d9c42cd4fc0b47b96611a3aa6c70cb7d/workoutTracking/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in response1["exercises"]:
    sheet_inputs={
        "workout":{
    "date":today_date,
    "time":now_time,
    "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]}}
headersAuth = {
    'Authorization': 'Basic '+ 'bnVsbDpudWxs',
}
response3= requests.post(url=website,json=sheet_inputs,headers=headersAuth)
print(response3.text)
