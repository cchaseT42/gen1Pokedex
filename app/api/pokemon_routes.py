from flask import Blueprint, jsonify, request
from app.models import Pokemon, db

pokemon_routes = Blueprint('pokemon', __name__)

@pokemon_routes.route('/<int:id>')
def get_pokemon(id):
    pokemon = db.session.query(Pokemon).filter_by(id = int(id))

    return {'pokemon': pokemon.to_dict()}
