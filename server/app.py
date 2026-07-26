from flask import Flask, make_response, jsonify
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
        
        body = [{'id' : workout.id, 
                    'date' : workout.date, 
                    'duration_minutes' : workout.duration_minutes, 
                    'notes' : workout.notes}
                    for workout in workouts]
    
        return make_response(body, 200)

    except ValidationError as err :
        print('Valid fields : ', err.valid_data)
        print('Invalid fields : ', err.message)






        


if __name__ == '__main__':
    app.run(port=5555, debug=True)