# Django-Moovies

### L'application en question est une application Python/Django développée dans le cadre d'une évaluation. Son objectif est de permettre à un utilisateur de rechercher des informations sur un film dans une base de données locale et, en cas de non-correspondance, d'interroger une API tierce (OMDB API) pour obtenir les résultats.

## Caractéristiques principales de cette application :

## Fonctionnalité de recherche de films :
* ### L'application présente un formulaire de recherche où l'utilisateur peut saisir le nom d'un film.
# Recherche dans la base de données locale :
* ### L'application interroge d'abord sa propre base de données pour trouver des correspondances avec le film recherché.
# Interrogation de l'API externe : 
* ### Si aucun résultat n'est trouvé dans la base de données locale, l'application utilise l'API OMDB pour obtenir les informations sur le film.
# Enregistrement des résultats :
* ### Les résultats obtenus à partir de l'API OMDB sont enregistrés dans la base de données locale pour une utilisation ultérieure, évitant ainsi de répéter la requête à l'API pour les mêmes films.
# Affichage des résultats :
* ### Les résultats de la recherche sont présentés à l'utilisateur, comprenant au minimum le titre du film, l'année de sortie et les genres.

# Fonctionaliter implementer :

* ### Espace Administrateur
* ### Realisation des tests