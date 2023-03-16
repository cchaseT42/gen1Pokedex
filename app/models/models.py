from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

def add_prefix_for_prod(attr):
    if environment == "production":
        return f"{SCHEMA}.{attr}"
    else:
        return attr


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    evolves = db.Column(db.Boolean, default=True)

class Moves(db.Model):
    __tablename__ = "moves"
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    accuracy = db.Column(db.Integer)
    tm_number = db.Column(db.Integer)
    type = db.Column(db.String, nullable=False)
    pp = db.Column(db.Integer, nullable=False)

pokemon_moves = db.Table(
    "pokemon_moves",
    db.Column(
        "pokemon_id",
        db.Integer,
        db.ForeignKey("pokemon.id"),
        primary_key=True
    ),
    db.Column(
        "moves_id",
        db.Integer,
        db.ForeignKey("moves.id"),
        primary_key=True
    )
)
