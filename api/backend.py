import csv
import sqlite3
import random
import json 
import os
from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
from pdb import set_trace
CSV_FILE = 'csv_new.csv'
CITY_ATTRIBUTE_FILE = 'city_attributes.csv'
DB_NAME = 'boersendaten.db'
DB_TABLE = 'original_csv_data'


app = Flask(__name__)
CORS(app)


conn = sqlite3.connect('DB_NAME')
cursor = conn.cursor()

def random_data():
    
    #Return a random json daten snippet. for Roberts gamification
    cursor.execute("SELECT 'Aktentitel FROM original_csv_data")

    rows = cursor.fetchall()
    random_row = random.randrange(0,len(rows))
    
    random_aktentitel = rows[random_row]

    return random_aktentitel



def random_data2(column):
    
    #Return a random json daten snippet. for Roberts gamification

    with open (CSV_FILE, 'r') as f:
            csv_data = csv.DictReader(f)
            rows = list(csv_data)
            random_row = random.randrange(0,len(rows))
            
            random_aktentitel = rows[random_row][column]

            return random_aktentitel


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
        

@app.route('/visualisation')
def visualisation():
    return render_template('visualisation.html')

@app.route('/', methods=['GET'])
def root():
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir,'api', 'dist'), 'index.html')

@app.route('/css/<path:path>', methods=['GET'])
def serve_css(path):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir,'api', 'dist','css'), path)

@app.route('/js/<path:path>', methods=['GET'])
def serve_js(path):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir,'api', 'dist','js'), path)    

@app.route('/api', methods=['GET'])
def get_tasks():
    return jsonify({'cities': city_attributes()})

@app.route('/robert', methods=['GET'])
def get_random_akten():
    return jsonify({'file': random_data()})

@app.route('/save', methods=['POST'])
def receive_updates():
    print(json.dumps(request.get_json()))
    return json.dumps(request.get_json())

if __name__ == '__main__':
    app.run(debug=True)
