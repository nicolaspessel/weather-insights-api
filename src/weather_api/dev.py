from pprint import pprint
from client import fetch_forecast

data = fetch_forecast(latitude=52, longitude=13)

print("== RESPOSTA FULL ==")
pprint(data)

print("\n == HOURLY ==")
pprint(data["hourly"])