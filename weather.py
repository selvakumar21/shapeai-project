import requests
from datetime import datetime

api_key = '575645e58398db248e98548211bda371'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data)
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
loc=location.upper()
print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
with open('records.txt','a') as f:
    f.write(loc+'\n')
    f.write("DATE TIME: "+date_time+"\n")
    f.write("TEMPERATURE: "+str(temp_city)+"\n")
    f.write("WEATHER: "+weather_desc+"\n")
    f.write("HUMIDITY: "+str(hmdt)+"\n")
    f.write("WIND SPEED: "+str(wind_spd)+"\n\n")
