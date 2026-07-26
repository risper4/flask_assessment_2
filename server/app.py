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
            body = {'error': f'Workout {id} not found'}
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
    try :
        data = request.get_json()
        workout = Workout(date = data['date'], duration_minutes = data['duration_minutes'], notes = data['notes'])
    
        db.session.add(workout)
        db.session.commit()
    
        result = ({
            'id' : workout.id, 
            'date' : workout.date, 
            'duration_minutes' : workout.duration_minutes, 
            'notes' : workout.notes
            })
    
        return make_response(result, 200)

    except ValidationError as err :
        print('Invalid field : ', err.message)
        print('Valid field : ', err.valid_data)



@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id) :
    try :
        workout = Workout.query.filter_all(id).first()
        
        if not workout :
            body = {'error' : f'Workout {id} not found'}
            status = 404

        else :
            db.session.delete(workout)
            db.session.commit()

    except ValidationError as err :
        print("Invalid field", err.message)



@app.route('/exercises', methods=['GET'])
def get_exercises() :
    try :
        exercises = Exercise.query.all()
        
        body = [{'id' : e.id, 'name' : e.name, 'category' :  e.category, 'equipment_needed' : e.equipment_needed} for e in exercises]
    
        return make_response(body, 200)

    except ValidationError as err :
        print('Invalid field' ,err.message)



@app.route('/exercises/<int:id>', methods=['GET'])
def get_specific_id(id) :
    try :
        e = Exercise.query.filter_by(id=id).first()

        if not e :
            body = {'error' : f'Exercise {id} not found'}
            status = 404

        else :
            body = {'id' : e.id, 'name' : e.name, 'category' :  e.category, 'equipment_needed' : e.equipment_needed}
            status = 200

        return make_response(body, status)

    except ValidationError as err :
        print('Invalid fields : ', err.messages)


@app.route('/exercises', methods=['POST'])
def add_exercise() :
    try :
        data = request.get_json()
        new_exercise = Exercise(name = data['name'], category = data['category'], equipment_needed = data['equipment_needed'])

        db.session.add(new_exercise)
        db.session.commit()

        result = {
            'id' : new_exercise.id,
            'name' : new_exercise.name,
            'category' : new_exercise.category,
            'equipment_needed' : new_exercise.equipment_needed
        }

        return make_response(result, 200)

    except ValidationError as err :
        print('Invalid fields : ', err.messages)


     
        


if __name__ == '__main__':
    app.run(port=5555, debug=True)