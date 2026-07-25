from app import app
from models import *

with app.app_context():

	# reset data and add new example data, committing to db 

    Exercise.query.delete()
    Workout.query.delete()
    WorkoutExercise.query.delete()

   