"""
Reacitiesities from the new csv file and get the coordinates from openstreetmamp. Return Dict/Json.
"""
import csv
import json


CSV_FILE = 'csv_new.csv'

def cities():
    """
    Return dict with the cities from new_csv.csv. 
    """
    with open (CSV_FILE , 'r') as f:
        csv_data = csv.DictReader(f)
        cities = {}
        for i in csv_data:
            if i['Stadt'] not in list(cities.keys()):
                cities[i['Stadt']] = {'len':'', 'lat':'', 'radius':''}
                print(str(i['Stadt']).encode('utf-8'))
        json_data = json.dumps(cities)

    #with open ('coordinates.json', 'w') as f:
    #    f.write(json_data)
    #print(json_data)

    return(cities) 

        
if __name__ == '__main__':
    cities()

