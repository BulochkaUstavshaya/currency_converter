from django.shortcuts import render

from .forms import CurrencyValueForm
from .services.currency import convert_currencies


def index(request):
    content = {}
    if request.method == 'POST':
        form = CurrencyValueForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            amount = round(convert_currencies(
                data['currency_from'],
                data['currency_into'],
                float(data['value'])
            ), 2)
            content['amount'] = amount

    else:
        form = CurrencyValueForm()

    content['form'] = form
    return render(request, 'currency_converter_app/index.html', content)

