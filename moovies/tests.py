from django.test import TestCase, Client
from django.urls import reverse
from .models import Movie
from django.contrib.messages import get_messages
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

    def test_search_no_movie(self):
        response = self.client.post(self.search_url, {'search_query': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moovie/searchFilm.html')
        self.assertTrue('movies' in response.context)
        self.assertFalse(Movie.objects.filter(title__icontains='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX').exists())
        self.assertTrue(len(response.context['movies']) == 0)
        self.assertTrue(response.context['form'].is_valid())
        self.assertTrue(response.context['form'].errors == {})

        #storage = response.wsgi_request.session.get('django.contrib.messages')
        #messages = list(get_messages(storage))

        #self.assertTrue(len(messages) == 1)

        #for message in messages:
           # print(message)

        #self.assertTrue(str(messages[0]) == "Aucun film trouvé pour cette recherche")