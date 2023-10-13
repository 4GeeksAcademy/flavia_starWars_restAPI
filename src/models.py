from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
        }

# STARSHIPS --------------------------------------------------------------------------------------------------------------------------------------------------------
class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    model = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)

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
    starship_data = db.relationship('Starships', backref='related_films')
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'))
    film_data = db.relationship('Films', backref='related_starships')

    def __repr__(self):
        return 'The relationship ID is {}'.format(self.id)
    
    def serialize(self):
        return {
            "id": self.id,
            "starship_data": self.starship_data.serialize(),
            "film_data": self.films_data.serialize()
        }

class Starships_Characters(db.Model):
    __tablename__ = 'starships_characters'
    id = db.Column(db.Integer, primary_key=True)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship_data = db.relationship('Starships', backref = 'related_characters')
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character_data = db.relationship('Characters', backref = 'related_starships')

    def __repr__(self):
        return 'The relationship ID is{}'.format(self.id)
    
    def serialize(self):
        return {
            "id": self.id,
            "starship_data": self.starship_data.serialize(),
            "character_data": self.character_data.serialize()
        }


class Favorite_Starships(db.Model):
    __tablename__ = 'favorite_starships'
    id = db.Column(db.Integer, primary_key=True)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship_data = db.relationship('Starships')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_data = db.relationship(User)

    def __repr__(self):
        return 'The favorite starship ID is {}'.format(self.id)
    
    def serialize(self):
        return {
            "favorite_id": self.id,
            "starship_data": self.starship_relationship.serialize()
        }

# PLANETS --------------------------------------------------------------------------------------------------------------------------------------------------------

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    rotation_period = db.Column(db.String(50), nullable=False)
    climate = db.Column(db.String(50), nullable=False)
    characters_relationship = db.relationship('Characters')
    species_relationship = db.relationship('Species', back_populates="planet_data")

    def __repr__(self):
        return '{}'.format(self.name)
    
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
    planet_data = db.relationship('Planets', backref = 'related_films')
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'))
    film_data = db.relationship('Films', backref = 'related_planets')

    def __repr__(self):
        return 'The relationship ID is {}'.format(self.id)
    
    def serialize(self):
        return {
            "id": self.id,
            "planet_data": self.planet_data.serialize(),
            "film_data": self.film_data.serialize()
        }

class Favorite_Planets(db.Model):
    __tablename__ = 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet_data = db.relationship('Planets')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_data = db.relationship(User)

    def __repr__(self):
        return 'The ID of the favorite planet is {}'.format(self.id)
    
    def serialize(self):
        return {
            "favorite_id": self.id,
            "planet_data": self.planet_relationship.serialize()
        }

# FILMS --------------------------------------------------------------------------------------------------------------------------------------------------------

class Films(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    episode = db.Column(db.Integer, unique=True, nullable=False)
    director = db.Column(db.String(50))

    def __repr__(self):
        return '{}'.format(self.title)
    
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "episode" : self.episode,
            "director": self.director
        }

class Films_Characters(db.Model):
    __tablename__ = 'films_characters'
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'))
    film_data = db.relationship('Films', backref = 'related_characters')
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character_data = db.relationship('Characters', backref = 'related_films')

    def __repr__(self):
        return 'The relationship ID is {}'.format(self.id)
    
    def serialize(self):
        return {
            "id": self.id,
            "film_data": self.film_data.serialize(),
            "character_data": self.character_data.serialize()
        }


class Films_Species(db.Model):
    __tablename__ = 'films_species'
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'))
    film_data = db.relationship('Films', backref = 'related_species')
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    species_data = db.relationship('Species', backref = 'related_films')

    def __repr__(self):
        return 'The relationship ID is {}'.format(self.id)
    
    def serialize(self):
        return {
            "id": self.id,
            "film_data": self.film_data.serialize(),
            "species_data": self.species_data.serialize()
        }


class Favorite_Films(db.Model):
    __tablename__ = 'favorite_films'
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'))
    film_data = db.relationship('Films')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_data = db.relationship(User)

    def __repr__(self):
        return 'The favorite planet ID is {}'.format(self.id)
    
    def serialize(self):
        return {
            "favorite_id": self.id,
            "film_data": self.film_relationship.serialize()
        }

# CHARACTERS --------------------------------------------------------------------------------------------------------------------------------------------------------

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet_data = relationship('Planets', back_populates='characters_relationship')
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    species_data = relationship('Species', back_populates='characters_relationship')

    def __repr__(self):
        return '{}'.format(self.name)
    
    def serialize(self):
        return {
            "id": self.id, 
            "name": self.name,
            "planet_data": self.planet_data.serialize(),
            "species_data": self.species_data.serialize_without_planet()
        }

class Favorite_Characters(db.Model):
    __tablename__ = 'favorite_characters'
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character_data = db.relationship('Characters')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    User_data = db.relationship(User)

    def __repr__(self):
        return 'The ID of the favorite film is {}'.format(self.id)
    
    def serialize(self):
        return {
            "favorite_id": self.id,
            "character_data": self.character_id_relationship.serialize()
        }

# SPECIES ---------------------------------------------------------------------------------------------------------------------------------------------------------------

class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    classification = db.Column(db.String(50))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet_data = relationship('Planets', back_populates="species_relationship")
    characters_relationship = relationship('Characters', back_populates="species_data")

    def __repr__(self):
        return '{}'.format(self.name)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
            "planet_data": self.planet_data.serialize()
        }
    def serialize_without_planet(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
        }

class Favorite_Species(db.Model):
    __tablename__ = 'favorite_species'
    id = db.Column(db.Integer, primary_key=True)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    species_data = db.relationship('Species')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_data = relationship(User)

    def __repr__(self):
        return 'The ID of the favorite species is {}'.format(self.id)
    
    def serialize(self):
        return {
            "favorite_id": self.id,
            "species_data": self.species_id_relationship.serialize()
        }

























