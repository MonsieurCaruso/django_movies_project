from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


# Create your views here.
def weather_view(request):
    API_KEY = 'e840120397fd69790c9ff22e5f354b0f'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY
    
    response = requests.get(url.format('Ulm'))
    if response.status_code == 200:
        data = response.json()
        formatted_data = json.dumps(data, indent=4)
        return HttpResponse(f'<pre>{formatted_data}</pre>')
    # Ergebnisse sammeln
    response_details = []
    for attr in dir(response):
        try:
            value = getattr(response, attr)
            response_details.append(f"<b>{attr}</b>: {value}<br>")
        except Exception as e:
            response_details.append(f"<b>{attr}</b>: Error - {e}<br>")

    # Als String zusammenfügen
    html_content = "".join(response_details)
    
    # In HttpResponse zurückgeben
    return HttpResponse(html_content, content_type="text/html")