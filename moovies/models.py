from django.db import models

class Movie(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    poster_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
