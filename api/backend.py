import csv
import random
from flask import Flask, render_template, jsonify
#from flask_restful import Resource, Api

CSV_FILE = 'csv_new.csv'

app = Flask(__name__)

"""
def random_data():
    
    #Return a random json daten snippet. for Roberts gamification
    

    with open (CSV_FILE, 'r') as f:
            csv_data = csv.DictReader(f)
            rows = list(csv_data)
            random_row = random.randrange(0,len(rows))
            
            random_aktentitel = rows[random_row]['Aktentitel']

            return random_aktentitel
"""

def city_points():
    """
    Some description...
    """
    cities = []
    with open ('city_list.csv', 'r') as f:
        csv_data = csv.DictReader(f)
        rows = list(csv_data)

        for i in rows:
            if i['lat'] != '0':
                cities.append({
                    "lat": i['lat'],
                    "lan": i['lon'],
                    "radius": i['Anzahl_Firmen']
                })
    return cities

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


@app.route('/api', methods=['GET'])
def get_tasks():
    return jsonify({'cities': city_points()})



if __name__ == '__main__':
    app.run(debug=True)
