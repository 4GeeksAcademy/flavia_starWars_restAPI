from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return 'The user name is {}'.format(self.name)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
        }

class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    model = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return 'The name of the spaceship is {}'.format(self.name)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model
        }

class Starships_Films(db.Model):
    __tablename__ = 'starships_films'
    id = db.Column(db.Integer, primary_key=True)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship_relationship = db.relationship('Starships')
    films_id = db.Column(db.Integer, db.ForeignKey('films.id'))
    films_relationship = db.relationship('Films')

class Starships_Characters(db.Model):
    __tablename__ = 'starships_characters'
    id = db.Column(db.Integer, primary_key=True)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship_relationship = db.relationship('Starships')
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    characters_relationship = db.relationship('Characters')

class Favorite_Starships(db.Model):
    __tablename__ = 'favorite_starships'
    id = db.Column(db.Integer, primary_key=True)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship_relationship = db.relationship('Starships')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_relationship = db.relationship(User)

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    rotation_period = db.Column(db.String(50), nullable=False)
    climate = db.Column(db.String(50), nullable=False)
    characters_relationship = db.relationship('Characters')
    species_relationship = db.relationship('Species')

    def __repr__(self):
        return 'The name of the planet is {}'.format(self.name)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "climate": self.climate
        }

class Planets_Films(db.Model):
    __tablename__ = 'planets_films'
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet_relationship = db.relationship('Planets')
    films_id = db.Column(db.Integer, db.ForeignKey('films.id'))
    films_relationship = db.relationship('Films')

class Favorite_Planets(db.Model):
    __tablename__ = 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet_relationship = db.relationship('Planets')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_relationship = db.relationship(User)

class Films(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    episode = db.Column(db.Integer, unique=True, nullable=False)
    director = db.Column(db.String(50))
    release_date = db.Column(db.Date)

class Films_Characters(db.Model):
    __tablename__ = 'films_characters'
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'))
    film_relationship = db.relationship('Films')
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    characters_relationship = db.relationship('Characters')

class Films_species(db.Model):
    __tablename__ = 'films_species'
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'))
    film_relationship = db.relationship('Films')
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    species_relationship = db.relationship('Species')

class Favorite_Films(db.Model):
    __tablename__ = 'favorite_films'
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'))
    film_relationship = db.relationship('Films')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_relationship = db.relationship(User)

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    planet = db.Column(db.Integer, db.ForeignKey('planets.id'))
    character = db.relationship('Species')

class Favorite_Characters(db.Model):
    __tablename__ = 'favorite_characters'
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character_id_relationship = db.relationship('Characters')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship(User)

class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    classification = db.Column(db.String(50))
    planet = db.Column(db.Integer, db.ForeignKey('planets.id'))
    character = db.Column(db.Integer, db.ForeignKey('characters.id'))

class Favorite_Species(db.Model):
    __tablename__ = 'favorite_species'
    id = db.Column(db.Integer, primary_key=True)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    species_id_relationship = db.relationship('Species')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_relationship = relationship(User)

























