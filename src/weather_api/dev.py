from pprint import pprint
from client import fetch_forecast
from service import summarize_forecast

forecast = fetch_forecast(latitude=52, longitude=13)

summary = summarize_forecast(forecast)

pprint(summary)