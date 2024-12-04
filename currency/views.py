from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
# Liste der gängigen Währungen
CURRENCY_CHOICES = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']

def currency(request):
    api_key = '55d50301c8add778a9ca4369'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/'

    conversion_result = None
    error_message = None

    if request.method == 'POST':
        from_currency = request.POST.get('from_currency', 'USD')
        to_currency = request.POST.get('to_currency', 'EUR')
        amount = request.POST.get('amount', 1)

        try:
            response = requests.get(url + from_currency)
            if response.status_code == 200:
                data = response.json()
                formatted_data = json.dumps(data, indent=4)
                #return HttpResponse(f'<pre>{formatted_data}</pre>')

                
                rates = data['conversion_rates']
                if to_currency in rates:
                    conversion_result = float(amount) * rates[to_currency]
                else:
                    error_message = f"Die Währung '{to_currency}' wird nicht unterstützt."
            else:
                error_message = "Fehler beim Abrufen der Wechselkurse. Bitte später erneut versuchen."
        except Exception as e:
            error_message = f"Ein Fehler ist aufgetreten: {e}"

    return render(request, 'currency/convert.html', {
        'conversion_result': conversion_result,
        'error_message': error_message,
        'currencies': CURRENCY_CHOICES,  # Währungen an das Template übergeben
    })