import requests


def get_weather(city):
    response =requests.get(f"https://wttr.in/{city}?format=j1")
    return response.json()['current_condition'][0]["FeelsLikeC"]

print(get_weather("Ahmedabad"))
print(get_weather("Surat"))