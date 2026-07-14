import os

import requests
import smtplib


from_mail = "akshay.gaonkar07@gmail.com"
password = "wiyubqxotxxqtfbh"

api_key = os.environ.get("OWM_API_KEY")
print(api_key)
# city_name = input("Please enter city name whose weather report you want to know: \n")
base_url = f"https://api.openweathermap.org/data/2.5/forecast"

def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(from_mail, password)
        connection.sendmail(from_mail, from_mail, "Subject: Weather forecast for Mumbai, India\n\n"
                                                  "Rain is expected within the next 12 hours. "
                                                  "Please remember to carry an umbrella with you.")

def get_weather():
    parameters = {
        "q": "Mumbai, India",
        "cnt": 4,
        "appid": api_key
    }
    response = requests.get(f"{base_url}", params=parameters)
    response.raise_for_status()
    data = response.json()
    list_data = data["list"]
    print(list_data)
    will_rain = False
    for item in list_data:
        weather_id = item["weather"][0]["id"]
        if weather_id < 700:
            will_rain = True
    if will_rain:
        # send_mail()
        print("Rain is expected")

get_weather()
