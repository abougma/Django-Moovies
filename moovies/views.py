from django.shortcuts import render
from .forms import FilmSearchForm
from .models import Movie
from django.http import HttpResponse
import requests

def search_film(request):
    form = FilmSearchForm()
    movies = []

    if request.method == 'POST':
        form = FilmSearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']

            movies_from_db = Movie.objects.filter(title__icontains=search_query)
            movies.extend(movies_from_db)

            if not movies_from_db:
                api_url = f'http://www.omdbapi.com/?apikey=2efdefdb&s={search_query}'
                try:
                    response = requests.get(api_url)
                    response.raise_for_status()
                    data = response.json()

                    if data.get('Search'):
                        for movie_data in data['Search']:
                            movie = Movie(title=movie_data['Title'], year=movie_data['Year'])

                            if movie_data.get('Poster'):
                                movie.poster_url = movie_data['Poster']
                            movie.save()
                            movies.append(movie)
                except requests.RequestException as e:
                    print(f"Erreur de requête à l'API OMDb : {e}")

    return render(request, 'moovie/searchFilm.html', {'form': form, 'movies': movies})