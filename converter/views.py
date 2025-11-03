from django.shortcuts import render
from .forms import CurrencyForm
from .services.currency import Currency
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def convert_currency(req):
    result = None

    form = CurrencyForm(req.POST)
    if form.is_valid():
        amount = form.cleaned_data['amount']
        currency_from = form.cleaned_data['currency_from']
        currency_to = form.cleaned_data['currency_to']

        converter = Currency()
        result = converter.convert(amount, currency_from, currency_to)

    return render(req, 'converter/index.html', {'form': form, 'result': result})
