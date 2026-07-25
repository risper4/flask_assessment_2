from app import app
from models import *

with app.app_context():

	# reset data and add new example data, committing to db 

    Exercise.query.delete()
    Workout.query.delete()
    WorkoutExercise.query.delete()

   
    e1 = Exercise(name='aerobics dance', category='cardio', equipment_needed=False)
    e2 = Exercise(name='pilates', category='flexibility', equipment_needed=True)
    e3 = Exercise(name='push-ups', category='bodyweight', equipment_needed=False)
    e4 = Exercise(name='tai-chi', category='balance', equipment_needed=True)
    e5 = Exercise(name='Arm work (Lifting weights)', category='weightlifting', equipment_needed=True)


    w1 = Workout(date='29/7/2026', duration_minutes=60, notes='Arrive early')
    w2 = Workout(date='1/8/2026', duration_minutes=45, notes='Register new members')
    w3 = Workout(date='12/8/2026', duration_minutes=90)
    w4 = Workout(date='15/8/2026', duration_minutes=60, notes='Equipment checks')
    w5 = Workout(date='20/8/2026', duration_minutes=45, notes='Recieve new equipment delivery')
    w6 = Workout(date='24/8/2026', duration_minutes=50)


    we1 = WorkoutExercise(reps=10, sets=3, duration_seconds=30, workout=w4, exercise=e1)
    we2 = WorkoutExercise(reps=12, sets=4, duration_seconds=40, workout=w1, exercise=e3)
    we3 = WorkoutExercise(reps=7, sets=2, duration_seconds=30, workout=w5, exercise=e2)
    we4 = WorkoutExercise(reps=5, sets=4, duration_seconds=45, workout=w6, exercise=e4)
    we5 = WorkoutExercise(reps=10, sets=2, duration_seconds=60, workout=w3, exercise=e2)
    we6 = WorkoutExercise(reps=5, sets=3, duration_seconds=50, workout=w2, exercise=e5)

   