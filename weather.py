import requests

city_name = "Bengaluru"
API_Key = '235b0aa66ce8cc432f2b412f970cff9f'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('weather is ',data['weather'][0]['description'])
    print('current temperature is',data['main']['temp'])
    print('current temperature feels like',data['main']['feels_like'])
    print('current humidity is',data['main']['humidity'])
    
    