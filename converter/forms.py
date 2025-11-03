from django import forms


class CurrencyForm(forms.Form):
    amount = forms.FloatField()
    currency_from = forms.CharField()
    currency_to = forms.CharField()
