from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from marshmallow import ValidationError, fields, validates, Schema, validates_schema, post_load
from datetime import date, datetime

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Exercise(db.Model) :
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False)

    workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise', cascade='all, delete-orphan')

    workouts = association_proxy(
        'workout_exercises',
        'workout',
        creator = lambda workout_obj : WorkoutExercise(workout=workout_obj)
    )

    @validates ('category')
    def validate_category(self, key, value) :
        category_list = ['cardio', 'flexibility', 'weightlifting', 'bodyweight', 'balance', 'intense']

        if value not in category_list:
            raise ValueError(f"Category selected must be one of these : {','.join(category_list)}")
        return value


    class ExerciseSchema(Schema) :
        id = fields.Int(dump_only=True)
        name = fields.String(required=True)
        category = fields.String(required=True)
        equipment_needed = fields.Boolean(required=True)
        workout_exercises = fields.List(fields.Nested(lambda : WorkoutExercise.WorkoutExerciseSchema(exclude=('workout', 'exercise'))))


    @validates_schema
    def no_of_categories (self, data, **kwargs) :
        if data.get('category') > 1 :
            raise ValidationError('Only one category should be chosen')



    
class Workout(db.Model) :
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String, nullable=True)

    workout_exercises = db.relationship('WorkoutExercise', back_populates='workout', cascade='all, delete-orphan')

    exercises = association_proxy(
        'workout_exercises',
        'exercise',
        creator = lambda exercise_obj : WorkoutExercise(exercise=exercise_obj)
    )

    __table_args__ = (
        db.CheckConstraint('(15 <= duration_minutes <= 100)'),
    )

    @validates('date')
    def validate_date(self, key, value) :
        if isinstance(value, str):
            value = datetime.strptime(value, '%d/%m/%Y').date()

        if value < date.today() :
            raise ValueError('Date set cannot be in the past')
        return value


    class WorkoutSchema(Schema) :
        id = fields.Integer(dump_only=True)
        date = fields.Date(required=True)
        duration_minutes = fields.Integer(required=True)
        notes = fields.String(required=True)
        workout_exercises = fields.List(fields.Nested(lambda : WorkoutExercise.WorkoutExerciseSchema(exclude=('workout', 'exercise'))))




class WorkoutExercise(db.Model):
    __tablename__ = 'WorkoutExercises'

    id = db.Column(db.Integer, primary_key=True)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    duration_seconds = db.Column(db.Integer)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)

    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')

    __table_args__ = (
        db.CheckConstraint ('(reps > sets) AND (reps >= 5)'),
    )

    class WorkoutExerciseSchema(Schema) :
        id = fields.Integer(dump_only=True)
        reps = fields.Integer(required=True)
        sets = fields.Integer(required=True)
        duration_seconds = fields.Integer()
        workout = fields.Nested(lambda : Workout.WorkoutSchema(exclude=('workout_exercises',)))
        exercise = fields.Nested(lambda : Exercise.ExerciseSchema(exclude=('workout_exercises',)))


    @validates_schema
    def check_sets_vs_duration_seconds(self, data, **kwargs):
        if data.get('sets') == 0  and data.get('duration_seconds') :
            raise ValidationError('There cannot be any duration seconds if there are no sets')


