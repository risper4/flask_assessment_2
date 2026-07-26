from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from marshmallow import ValidationError

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/workouts', methods=['GET'])
def get_workouts() :
    try :
        workouts = Workout.query.all()
        
        body = [{
                    'id' : workout.id, 
                    'date' : workout.date, 
                    'duration_minutes' : workout.duration_minutes, 
                    'notes' : workout.notes}
                    for workout in workouts]
    
        return make_response(body, 200)

    except ValidationError as err :
        print('Valid fields : ', err.valid_data)
        print('Invalid fields : ', err.message)



@app.route('/workouts/<int:id>', methods=['GET'])
def get_specific_workout(id)  :
    try :
        workout = Workout.query.filter_by(id=id).first()

        if not  workout :
            body = {f'error': 'Workout {id} not found'}
            status = 404
        else :
            body = {
                'id' : workout.id, 
                'date' : workout.date, 
                'duration_minutes' : workout.duration_minutes, 
                'notes' : workout.notes
                }
            status = 200

        return make_response(body, status)

    except ValidationError as err :
        print('Valid fields : ', err.valid_data)
        print('Invalid fields : ', err.messages)



@app.route('/workouts', methods=['POST'])
def add_workouts() :
    data = request.get_json()
    workout = Workout(date = data['date'], duration_minutes = data['duration_minutes'], notes = data['notes'])

    db.session.add(workout)
    db.session.commit()

    result = ({
        'id' : workout.id, 
        'date' : workout.date, 
        'duration_minutes' : workout.duration_minutes, 
        'notes' : workout.notes
        }, 'has been added')

    return make_response(result, 200)





        


if __name__ == '__main__':
    app.run(port=5555, debug=True)