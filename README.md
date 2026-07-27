# Flask SQLAlchemy Workout Application Backend

### By : Risper Gichia

## Introduction

* The workout application backend system includes :
        - Endpoints
        - SQLite Database


* The workout application backend system can :
        - Enlists all workouts
        - Displays a specific workout
        - Creates a new workout
        - Deletes a specific workout
        - Enlists all exercises
        - Displays a specific exercise
        - Creates a new exercise
        - Deletes a specific exercise
        - Creates a new workout_exercise instance


## Installation instructions
* The installations of the database are as follows  :
    
    1. App
        - pipenv install
        - pipenv shell
    
    2. Database (models.py)
        - flask db init
        - flask db migrate -m 'message about your migration here'
        - flask db upgrade head

    3. Seeding (seed.py)
        - python3 seed.py

    4. Running endpoints (app.py)
        - python3 app.py


## Endpoint access

    - Enlist all workout : `http://127.0.0.1:5555/workouts`

    - Display a specific workout : `http://127.0.0.1:5555/workouts/id`

    - Add a new workout : `http://127.0.0.1:5555/workouts`

    - Delete a specific workout : `http://127.0.0.1:5555/workouts/id`

    - Enlist all exercises : `http://127.0.0.1:5555/exercises`

    - Display a specific exercises : `http://127.0.0.1:5555/exercises/id`

    - Add a new exercises : `http://127.0.0.1:5555/exercises`

     - Delete a specific exercises : `http://127.0.0.1:5555/exercises/id`

     - Add a new workout_exercises : `http://127.0.0.1:5555/workouts/id/exercises/id/workout_exercises`


## Dependancies
    - Flask = "2.2.2"
    - Flask-Migrate = "3.1.0"
    - flask-sqlalchemy = "3.0.3"
    - Werkzeug = "2.2.2"
    - importlib-metadata = "6.0.0"
    - importlib-resources = "5.10.0"
    - ipdb = "0.13.9"
    - marshmallow = "3.20.1"

        
### Access
* Github : `https://github.com/risper4/flask_assessment_2.git`


### Contact 
    * Github : `risper4`
