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
from models import db, User, Starships, Planets
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

@app.route('/user', methods=['POST'])
def handle_newuser():
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

@app.route('/user', methods=['GET'])
def handle_allusers():
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

@app.route('/starships', methods=['POST'])
def handle_newstarship():
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

@app.route('/starships', methods=['GET'])
def handle_allstarships():
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

@app.route('/planets', methods=['POST'])
def handle_newplanet():
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

@app.route('/planets', methods=['GET'])
def handle_allplanets():
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


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
