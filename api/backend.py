import csv
import random
from flask import Flask, render_template, jsonify
#from flask_restful import Resource, Api


CSV_FILE = 'csv_new.csv'

app = Flask(__name__)
##api = Api(app)

def random_data():
    """
    Return a random json daten snippet.
    """

    with open (CSV_FILE, 'r') as f:
            csv_data = csv.DictReader(f)
            rows = list(csv_data)
            random_row = random.randrange(0,len(rows))
            
            random_aktentitel = rows[random_row]['Aktentitel']

            return random_aktentitel


cities = [
        {
            "lat": "51.3391827",
            "lan": "12.3810549",
            "radius": "300"

        },
        {
            "lat": "51.3391827",
            "lan": "12.3910549",
            "radius": "400"

        },
        {
            "lat": "51.3591827",
            "lan": "12.3710549",
            "radius": "200"

        }]


@app.route('/')
def root():
    return render_template('visualisation.html')

'''
class HelloWorld(Resource):
    def get(self):

        


        return {cities}

api.add_resource(HelloWorld, '/api')

'''

@app.route('/api', methods=['GET'])
def get_tasks():
    return jsonify({'cities': cities})



if __name__ == '__main__':
    app.run(debug=True)
