from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Exercise(db.Model) :
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)


class Workout(db.Model) :
    __tablename__ = 'workouts'


class WorkoutExercises(db.Model):
    __tablename__ = 'WorkoutExercises'