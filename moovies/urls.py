from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_film, name='search_film'),
]
