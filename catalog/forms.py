from django import forms


class SearchTermForm(forms.Form):
    search_term = forms.CharField(required=True)

