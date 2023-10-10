"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Starships, Planets, Films, Characters, Species
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/usuario', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# ENDPOINTS DE USER
@app.route('/user', methods=['POST', 'GET'])
def handle_allusers():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is None:
            return jsonify({'msg': 'The request body is null'}), 400
        if 'name' not in body: 
            return jsonify({'msg': 'Specify name'}), 400
        if 'age' not in body: 
            return jsonify({'msg': 'Specify age'}), 400
        if 'email' not in body: 
            return jsonify({'msg': 'Specify email'}), 400
        user = User()
        user.name = body['name']
        user.age = body['age']
        user.email = body['email']
        db.session.add(user)
        db.session.commit()
        return jsonify({'msg': 'User successfully added'}), 200
    if request.method == 'GET':
        users = User.query.all()
        users = list(map(lambda x: x.serialize(), users))
        return jsonify(users)

@app.route('/user/<int:user_id>', methods=['GET', 'PUT'])
def handle_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'msg': 'User do not exist'}), 400
    if request.method == 'GET':
        return jsonify(user.serialize())
    if request.method == 'PUT':
        body = request.get_json(silent=True)
        if body is None:
            return jsonify({'msg': 'Body cannot be empty'}), 400
        if 'name' in body:
            user.name = body['name']
        if 'age' in body:
            user.age = body['age']
        if 'email' in body: 
            user.email = body['email']
        db.session.commit()
        return jsonify({'msg': 'Updated user with ID {}'.format(user_id)}), 200

# ENDPOINTS DE STARSHIPS
@app.route('/starships', methods=['POST', 'GET'])
def handle_allstarships():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is None:
            return jsonify({'msg': 'Body cannot be empty'}), 400
        if 'name' not in body:
            return jsonify({'msg': 'Specify name'}), 400
        if 'model' not in body:
            return jsonify({'msg': 'Specify model'}), 400
        starships = Starships()
        starships.name = body['name']
        starships.model = body['model']
        db.session.add(starships)
        db.session.commit()
        return jsonify({'msg': 'Starship successfully added'}), 200
    if request.method == 'GET':
        starships = Starships.query.all()
        starships = list(map(lambda x: x.serialize(), starships))
        return jsonify(starships)

@app.route('/starships/<int:starships_id>', methods=['GET', 'PUT'])
def handle_starship(starships_id):
    starship = Starships.query.get(starships_id)
    if starship is None:
        return jsonify({'msg': 'Starships do not exist'}), 400
    if request.method == 'GET':
        return jsonify(starship.serialize())
    if request.method == 'PUT':
        body = request.get_json(silent=True)
        if body is None:
            return jsonify({'msg': 'Body cannot be empty'}), 400
        if 'name' in body:
            starship.name = body['name']
        if 'model' in body: 
            starship.model = body['model']  
        db.session.commit()
        return jsonify({'msg': 'Updated starship with ID {}'.format(starships_id)})
    
# ENDPOINTS DE PLANETS
@app.route('/planets', methods=['POST', 'GET'])
def handle_allplanets():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is None:
            return jsonify({'msg': 'Body cannot be empty'}), 400
        if 'name' not in body:
            return jsonify({'msg': 'Specify name'}), 400
        if 'rotation_period' not in body:
            return jsonify({'msg': 'Specify rotation_period'}), 400
        if 'climate' not in body:
            return jsonify({'msg': 'Specify climate'}), 400
        planets = Planets()
        planets.name = body['name']
        planets.rotation_period = body['rotation_period']
        planets.climate = body['climate']
        db.session.add(planets)
        db.session.commit()
        return jsonify({'msg': 'Planet successfully added'}), 200
    if request.method == 'GET':
        planets = Planets.query.all()
        planets = list(map(lambda x: x.serialize(), planets))
        return jsonify(planets)

@app.route('/planets/<int:planets_id>', methods=['GET', 'PUT'])
def handle_planet(planets_id):
    planets = Planets.query.get(planets_id)
    if planets is None:
        return jsonify({'msg': 'planets do not exist'}), 400
    if request.method == 'GET':
        return jsonify(planets.serialize())
    if request.method == 'PUT':
        body = request.get_json(silent=True)
        if body is None:
            return jsonify({'msg': 'Body cannot be empty'}), 400
        if 'name' in body:
            planets.name = body['name']
        if 'rotation_period' in body:
            planets.rotation_period = body['rotation_period']
        if 'climate' in body:
            planets.climate = body['climate'] 
        db.session.commit()
        return jsonify({'msg': 'Updated planet with ID {}'.format(planets_id)})

# ENDPOINTS DE FILMS
@app.route('/films', methods=['POST', 'GET'])
def handle_newfilm():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is None:
            return jsonify({'msg': 'Body cannot be empty'}), 400
        if 'title' not in body: 
            return jsonify({'msg': 'Specify title'}), 400
        if 'episode' not in body:
            return jsonify({'msg': 'Specify episode'}), 400
        if 'director' not in body:
            return jsonify({'msg': 'Specify director'}), 400
        film = Films()
        film.title = body['title']
        film.episode = body['episode']
        film.director = body['director']
        db.session.add(film)
        db.session.commit()
        return jsonify({'msg': 'Film successfully added'}), 200
    if request.method == 'GET':
        films = Films.query.all()
        films = list(map(lambda x: x.serialize(), films))
        return jsonify(films)
        
@app.route('/films/<int:films_id>', methods=['GET', 'PUT'])
def handle_film(films_id):
    film = Films.query.get(films_id)
    if request.method == 'GET':
        return jsonify(film.serialize())
    if request.method == 'PUT': 
        body = request.get_json(silent=True)
        if body is None:
            return jsonify({'msg': 'Body cannot be empty'}), 400
        if 'title' in body:
            film.title = body['title']
        if 'episode' in body:
            film.episode = body['episode']
        if 'director' in body:
            film.director = body['director']
        db.session.commit()
        return jsonify({'msg': 'Updated film with ID {}'.format(films_id)}), 200

# ENDPOINTS DE CHARACTERS
@app.route('/characters', methods=['POST', 'GET'])
def handle_allcharacters():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is None: 
            return jsonify({'msg': 'Body cannot be empty'}), 400
        character = Characters()
        character.name = body['name']
        db.session.add(character)
        db.session.commit()
        return jsonify({'msg': 'Character successfully added'}), 200
    
    if request.method == 'GET':
        characters = Characters.query.all()
        characters = list(map(lambda x: x.serialize(), characters))
        return jsonify(characters), 200
    
@app.route('/characters/<int:characters_id>', methods=['GET', 'PUT'])
def handle_character(characters_id):
    character = Characters.query.get(characters_id)
    if request.method == 'GET':
        return jsonify(character.serialize())
    if request.method == 'PUT':
        body = request.get_json(silent=True)
        if body is None: 
            return jsonify({'msg': 'Body cannot be empty'}), 400
        if 'name' in body: 
            character.name = body['name']
            db.session.commit()
            return jsonify({'msg': 'Updated character with ID {}'.format(characters_id)}), 200

# ENPOINTS DE SPECIES
@app.route('/species', methods=['POST', 'GET'])
def handle_allspecies():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is None:
            return jsonify({'msg': 'Body cannot be empty'}), 400
        species = Species()
        species.name = body['name']
        species.classification = body['classification']
        db.session.add(species)
        db.session.commit()
        return jsonify({'msg': 'Species succesfully added'}), 200
    if request.method == 'GET':
        species = Species.query.all()
        species = list(map(lambda x: x.serialize(), species))
        return jsonify(species), 200

@app.route('/species/<int:species_id>', methods=['GET', 'PUT'])
def handle_species(species_id):
    species = Species.query.get(species_id)
    if request.method == 'GET':
        return jsonify(species.serialize()), 200
    if request.method == 'PUT':
        body = request.get_json(silent=True)
        if body is None:
            return jsonify({'msg': 'Body cannot be empty'}), 400
        if 'name' in body:
            species.name = body['name']
        if 'classification' in body:
            species.classification = body['classification']
        db.session.commit()
        return jsonify({'msg': 'Updated species with ID {}'.format(species_id)})

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
