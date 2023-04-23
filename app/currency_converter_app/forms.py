from django import forms
from .services.currency import get_currency_names


class CurrencyValueForm(forms.Form):
    currency_name = get_currency_names()
    value = forms.FloatField(label='У меня есть')
    currency_from = forms.ChoiceField(choices=currency_name, label='')
    currency_into = forms.ChoiceField(choices=currency_name, label='Хочу перевести в')