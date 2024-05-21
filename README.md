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

# Guide d'utilisation :

### 1-Installer les dépendances

#### Pour installer les dépendances d'un projet, suivez ces étapes :

* #### Ouvrez votre terminal (Git Bash, PowerShell, Command Prompt, ou terminal intégré de votre IDE).
* #### Assurez-vous d'être dans le répertoire du projet, où se trouve le fichier requirements.txt.
* #### Utilisez pip pour installer les dépendances : pip install -r requirements.txt

### 2-Exécuter le projet

* #### Après avoir installé les dépendances, vous pouvez exécuter le serveur Django comme décrit précédemment : python manage.py runserver

### Guide complet révisé :

* #### Accédez à la page principale du dépôt sur GitHub.com.
* #### Au-dessus de la liste des fichiers, cliquez sur le bouton <> Code.
* #### Copiez l’URL du dépôt.
* #### Ouvrez Git Bash.
* #### Naviguez vers le répertoire où vous souhaitez cloner le dépôt en utilisant la commande cd (par exemple, cd /chemin/vers/repertoire).
* #### Tapez git clone, puis collez l’URL que vous avez copiée précédemment.


* #### git clone https://github.com/utilisateur/nom-du-depot.git

* #### Appuyez sur Entrée pour créer votre clone local.
* #### Ouvrez le dossier cloné dans un IDE où Django est installé.
* #### Installez les dépendances : pip install -r requirements.txt

* #### Dans le terminal de l'IDE, tapez : python manage.py runserver pour démarrer le projet.
* #### Dans le terminal, cliquez sur l'URL suivante : http://127.0.0.1:8000/

* #### Vous verrez alors la page d'accueil du projet Django.