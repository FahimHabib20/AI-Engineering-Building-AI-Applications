# The requests libary (htps for humans)
import requests
url = 'https://open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m'
response = requests.get(url) #  get requests
# print(response.json())
print(response.status_code)
print(response.headers)
print(response.text)
data = response.json()
print(data)