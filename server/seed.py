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
    e5 = Exercise('Arm work (Lifting weights)', 'weightlifting', True)


    w1 = Workout('29/7/2026', 60, 'Arrive early')
    w2 = Workout('1/8/2026', 45, 'Register new members')
    w3 = Workout('12/8/2026', 90)
    w4 = Workout('15/8/2026', 60, 'Equipment checks')
    w5 = Workout('20/8/2026', 45, 'Recieve new equipment delivery')
    w6 = Workout('24/8/2026', 50)

   