<a href="https://www.breatheco.de"><img height="280" align="right" src="https://github.com/4GeeksAcademy/flask-rest-hello/blob/main/docs/assets/badge.png?raw=true"></a>

# Flask Boilerplate for Junior Developers

## Test ready-made endpoints :)

SINGLE TABLES
```bash
--------- USER -----------------------
'/user', methods=['POST', 'GET'] # (post) add new users and (get) obtain all added users
'/user/<int:user_id>', methods=['GET', 'PUT'] # (get) obtain the information of a particular user and (put) modify data of a particular user
'/user/<int:user_id>/favorites', methods=['GET'] # (get) to obtain the favourites of all the sections of a specific user
--------- STARSHIPS ---------------------
'/starships', methods=['POST', 'GET'] # (post) add new starships and (get) obtain all added starships
'/starships/<int:starships_id>', methods=['GET', 'PUT'] # (get) obtain the information of a given starship and (put) modify data of a given starship
---------- PLANETS -----------------------
'/planets', methods=['POST', 'GET'] # (post) add new planets and (get) obtain all added planets
'/planets/<int:planets_id>', methods=['GET', 'PUT'] # (get) obtain the information of a particular planet and (put) modify data of a particular planet
---------- FILMS -------------------------
'/films', methods=['POST', 'GET'] # (post) add new films and (get) obtain all added films
'/films/<int:films_id>', methods=['GET', 'PUT'] # (get) obtain the information of a particular film and (put) modify data of a particular film
---------- CHARACTERS --------------------
'/characters', methods=['POST', 'GET'] # (post) add new characters and (get) obtain all added characters
'/characters/<int:characters_id>', methods=['GET', 'PUT'] # (get) obtain the information of a given character and (put) modify data of a given character
---------- SPECIES -----------------------
'/species', methods=['POST', 'GET'] # (post) add new species and (get) obtain all added species
'/species/<int:species_id>', methods=['GET', 'PUT'] # (get) obtain the information of a given species and (put) modify data of a given species
```
FAVORITES 
```bash
--------- FAVORITE STARSHIPS ------------
'/favorite_starships', methods=['GET'] # admin endpoint // (get) view all favourite starships with their corresponding users
'/favorite_starships/<int:starship_id>', methods=['GET', 'DELETE'] # admin endpoint // (get) to see all the times a particular starship was added to favourites and (delete) to remove from favourites all instances containing a particular starship
'/user/<int:user_id>/favorite_starships', methods=['GET', 'POST'] # (post) add starship to a particular user and (get) view the favourite starships of a particular user
'/user/<int:user_id>/favorite_starships/<int:starship_id>', methods=['GET', 'DELETE'] # (get) to individually view a particular starship of a particular user and (delete) to remove a particular starship from the favourites of a particular user
--------- FAVORITE PLANETS -------------
'/favorite_planets', methods=['GET'] # admin endpoint // (get) view all favourite planets with their corresponding users
'/favorite_planets/<int:planet_id>', methods=['GET', 'DELETE'] # admin endpoint // (get) to see all the times a particular planet was added to favourites and (delete) to remove all instances containing a particular planet from favourites
'/user/<int:user_id>/favorite_planets', methods=['GET', 'POST'] # (post) add planets to a particular user and (get) view a particular user's favourite planets
'/user/<int:user_id>/favorite_planets/<int:planet_id>', methods=['GET', 'DELETE'] # (get) to individually view a particular planet for a particular user and (delete) to remove a particular planet from a particular user's favourites
------- FAVORITE FILMS -----------------
'/favorite_films', methods=['GET'] # admin endpoint // (get) view all favourite films with their corresponding users
'/favorite_films/<int:film_id>', methods=['GET', 'DELETE'] # admin endpoint // (get) to see all the times a particular film was added to favourites and (delete) to remove all instances containing a particular film from favourites
'/user/<int:user_id>/favorite_films', methods=['POST', 'GET'] # (post) add films to a particular user and (get) view the favourite films of a particular user
'/user/<int:user_id>/favorite_films/<int:film_id>', methods=['GET', 'DELETE'] # (get) to individually view a particular film for a particular user and (delete) to delete a particular film from a particular user's favourites.
-------- FAVORITE CHARACTERS ------------
'/favorite_characters', methods=['GET'] # admin endpoint // (get) view all favourite characters with their corresponding users
'/favorite_characters/<int:character_id>', methods=['GET', 'DELETE'] # admin endpoint // (get) to see all the times a particular character was added to favourites and (delete) to remove from favourites all instances containing a particular character
'/user/<int:user_id>/favorite_characters', methods=['POST', 'GET'] # (post) add characters to a particular user and (get) view the favourite characters of a particular user
'/user/<int:user_id>/favorite_characters/<int:character_id>', methods=['GET', 'DELETE'] # (get) to individually view a particular character for a particular user and (delete) to delete a particular character from a particular user's favourites
-------- FAVORITE SPECIES --------------
'/favorite_species', methods=['GET'] # admin endpoint // (get) view all favourite species with their corresponding users
'/favorite_species/<int:species_id>', methods=['GET', 'DELETE'] # admin endpoint // (get) to see all the times a particular species was added to favourites and (delete) to remove all instances containing a particular species from favourites
'/user/<int:user_id>/favorite_species', methods=['POST', 'GET'] # (post) add species to a particular user and (get) view the favourite species of a particular user
'/user/<int:user_id>/favorite_species/<int:species_id>', methods=['GET', 'DELETE'] # (get) to view individually the specific species of a specific user and (delete) to delete a specific species from the favourites of a specific user
```
Create flask API's in minutes, [📹 watch the video tutorial](https://youtu.be/ORxQ-K3BzQA).

- [Extensive documentation here](https://start.4geeksacademy.com).
- Integrated with Pipenv for package managing.
- Fast deloyment to render.com or heroku with `$ pipenv run deploy`.
- Use of `.env` file.
- SQLAlchemy integration for database abstraction.

## 1) Installation

This template installs itself in a few seconds if you open it for free with Codespaces (recommended) or Gitpod.
Skip this installation steps and jump to step 2 if you decide to use any of those services.

> Important: The boiplerplate is made for python 3.10 but you can change the `python_version` on the Pipfile.

The following steps are automatically runned withing gitpod, if you are doing a local installation you have to do them manually:

```sh
pipenv install;
psql -U root -c 'CREATE DATABASE example;'
pipenv run init;
pipenv run migrate;
pipenv run upgrade;
```

## 2) How to Start coding

There is an example API working with an example database. All your application code should be written inside the `./src/` folder.

- src/main.py (it's where your endpoints should be coded)
- src/models.py (your database tables and serialization logic)
- src/utils.py (some reusable classes and functions)
- src/admin.py (add your models to the admin and manage your data easily)

For a more detailed explanation, look for the tutorial inside the `docs` folder.

## Remember to migrate every time you change your models

You have to migrate and upgrade the migrations for every update you make to your models:

```bash
$ pipenv run migrate # (to make the migrations)
$ pipenv run upgrade  # (to update your databse with the migrations)
```

## Check your API live

1. Once you run the `pipenv run start` command your API will start running live and you can open it by clicking in the "ports" tab and then clicking "open browser".

> ✋ If you are working on a coding cloud like [Codespaces](https://docs.github.com/en/codespaces/developing-in-codespaces/forwarding-ports-in-your-codespace#sharing-a-port) or [Gitpod](https://www.gitpod.io/docs/configure/workspaces/ports#configure-port-visibility) make sure that your forwared port is public.

## Publish/Deploy your website!

This boilerplate it's 100% read to deploy with Render.com and Herkou in a matter of minutes. Please read the [official documentation about it](https://start.4geeksacademy.com/deploy).

### Contributors

This template was built as part of the 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Find out more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer), and [Data Science Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning).

You can find other templates and resources like this at the [school github page](https://github.com/4geeksacademy/).
