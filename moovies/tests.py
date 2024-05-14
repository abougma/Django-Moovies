from django.test import TestCase, Client
from django.urls import reverse
from .models import Movie

class MovieSearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.search_url = reverse('search_film')

    def test_search_view(self):
        response = self.client.get(self.search_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moovie/searchFilm.html')

    def test_search_movie(self):
        response = self.client.post(self.search_url, {'search_query': 'Star Wars'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moovie/searchFilm.html')
        self.assertTrue('movies' in response.context)
        self.assertTrue(Movie.objects.filter(title__icontains='Star Wars').exists())



