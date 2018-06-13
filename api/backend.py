import csv
import random
from flask import Flask, render_template, jsonify

CSV_FILE = 'csv_new.csv'
CITY_ATTRIBUTE_FILE = 'city_attributes.csv'
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

def city_attributes():
    """
    Return coordinates and number of companies for each city.
    """
    city_attributes = []

    try:
        with open (CITY_ATTRIBUTE_FILE, 'r') as f:
            csv_data = csv.DictReader(f)
            rows = list(csv_data)

            for i in rows:
                if i['lat'] != '0':
                    city_attributes.append({
                        "lat": i['lat'],
                        "lan": i['lon'],
                        "radius": i['Anzahl_Firmen']
                    })
            return city_attributes
        
    except FileNotFoundError:
        print(CITY_ATTRIBUTE_FILE, 'not found..')
        

@app.route('/')
def root():
    return render_template('visualisation.html')


@app.route('/api', methods=['GET'])
def get_tasks():
    return jsonify({'cities': city_attributes()})



if __name__ == '__main__':
    app.run(debug=True)
