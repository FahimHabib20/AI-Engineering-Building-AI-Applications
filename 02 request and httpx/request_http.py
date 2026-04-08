import requests
import httpx
url = 'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'

response = requests.get(url)

print(response.status_code)   # check first
print(response.text[:200])    # debug
print(response.headers)
data = response.json()        # safe now
print(data)

