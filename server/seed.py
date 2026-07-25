from app import app
from models import *

with app.app_context():

	# reset data and add new example data, committing to db 

    Exercise.query.delete()
    Workout.query.delete()
    WorkoutExercise.query.delete()

   
    e1 = Exercise('aerobics dance', 'cardio', False)
    e2 = Exercise('pilates', 'flexibility', True)
    e3 = Exercise('push-ups', 'bodyweight', False)
    e4 = Exercise('tai-chi', 'balance', True)
    e5 = Exercise('Lifting dumbells', 'weightlifting', True)

    
   