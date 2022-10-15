from requests import get
key = "7ead771991e98833da03419ea00e22d6"
lat = ""
lon = ""

# api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
api2 = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={key}"

res = get(api2)
print(res.json())

# print(api2)
