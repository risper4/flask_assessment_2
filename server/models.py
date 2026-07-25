from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Exercise(db.Model) :
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)

    workout_exercises = db.relationship('WorkoutExercise', back_populate='exercise')

    workouts = association_proxy(
        'workout_exercises',
        'workout',
        creator = lambda workout_obj : WorkoutExercise(workout=workout_obj)
    )
    

class Workout(db.Model) :
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.String)

    workout_exercises = db.relationship('WorkoutExercise', back_populate='workout')

    exercises = association_proxy(
        'workout_exercises',
        'exercise',
        creator = lambda exercise_obj : WorkoutExercise(exercise=exercise_obj)
    )

    __table_args__ = (
        db.CheckConstraint('(15 <= duration_minutes <= 100)', )
    )


class WorkoutExercise(db.Model):
    __tablename__ = 'WorkoutExercises'

    id = db.Column(db.Integer, primary_key=True)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

    exercise = db.relationship('Exercise', back_populate='workout_exercises')
    workout = db.relationship('Workout', back_populate='workout_exercises')
