from django import forms

class FilmSearchForm(forms.Form):
    search_query = forms.CharField(label='Rechercher un film', max_length=100)
