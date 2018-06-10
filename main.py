import json,requests

## -------------------------------- Getting data from the city.list.json file and getting the choosen's city id ---------------------------------------------------
city_list_json = open("city.list.json", "r", encoding = "utf-8")

data = json.load(city_list_json)

# Get all the city's names
city_names = [data[i]["name"] for i in range(len(data))]

# User input
choosen_city = input("City name: ")
choosen_city.capitalize()

def findIndex(list_names,city_name):
    if city_name in list_names:
        city_index = list_names.index(city_name)
        return city_index
    else:
        return "An error has occurred. Did you write the city name right?"

def findID(list, city_index):
    return list[city_index]["id"]

city_id = findID(data, findIndex(city_names, choosen_city))
city_list_json.close()

## -----------------------------------------------Weather Data------------------------------------------------------------------

openweather_key = "f908f7c05b3be47e408fbfdf3a3c5be2"

r = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&APPID={openweather_key}")
city_data = r.json()

## ----------------------------------------------Formatting and Printing --------------------------------------------------------

temps = {
    'avg' : city_data["main"]["temp"],
    'max' : city_data["main"]["temp_max"],
    'min' : city_data["main"]["temp_min"]
}

humidity = str(city_data["main"]["humidity"]) + " %"

weather_desc = city_data["weather"][0]["description"]
weather = city_data["weather"][0]["main"]

print(f"City:            {choosen_city}\n")
print(f"Temperatures:    Average: {temps['avg']} °C\n                 Maximum: {temps['max']} °C\n                 Minimum: {temps['min']} °C\n")
print(f"Humidity:        {humidity}\n")
print(f"Weather:         {weather}:\n                 {weather_desc}\n\n")
