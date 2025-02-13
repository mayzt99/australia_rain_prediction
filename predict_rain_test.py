import requests

url = 'http://localhost:9696/predict_rain'

weather_info = {'location': 'hobart',
 'mintemp': 5.3,
 'maxtemp': 12.8,
 'rainfall': 3.2,
 'evaporation': 0.4,
 'sunshine': 5.6,
 'windgustdir': 'sw',
 'windgustspeed': 56.0,
 'winddir9am': 'ssw',
 'winddir3pm': 'ssw',
 'windspeed9am': 15.0,
 'windspeed3pm': 15.0,
 'humidity9am': 64.0,
 'humidity3pm': 56.0,
 'pressure9am': 1004.6,
 'pressure3pm': 1002.4,
 'cloud9am': 2.0,
 'cloud3pm': 5.0,
 'temp9am': 11.1,
 'temp3pm': 10.9,
 'raintoday': 'yes'}

response = requests.post(url, json=weather_info).json()
print(response)