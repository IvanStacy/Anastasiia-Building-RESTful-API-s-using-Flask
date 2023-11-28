from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=True)
    gender = db.Column(db.String(80), unique=False, nullable=True)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "birth_year": self.birth_year
        }
    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=True)
    population = db.Column(db.Integer, unique=False, nullable=True)
    orbital_period = db.Column(db.Float, unique=False, nullable=False)
    gravity = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity
        }
    
class Favorites(db.Model):
    
    favorite_id = db.Column(db.String(120), unique=False, nullable=False)
    favorite_type = db.Colunm(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Favorites %r>' % self.name

    def serialize(self):
        return {
            "favorite_id": self.favorite_id,
            "favorite_type": self.favorite_type
        
        }