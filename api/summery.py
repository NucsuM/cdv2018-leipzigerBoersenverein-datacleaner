import csv
import time
from geopy.geocoders import Nominatim
geolocator = Nominatim()


CSV_FILE = 'csv_new.csv'

def get_coordinates(city):
    """
    Get coordinates from openstreetmap via geopy. Does not work yet.
    """
    time.sleep(2)
    try:
        location = geolocator.geocode(city)
        lat = location.latitude
        lon = location.longitude
        print(city, '-->', 'lat: ', lat, ' lon', lon)
    except AttributeError as e:
        return (1)



class CityCoordinates():
    """
    Just a test to get some, not all, city coordinates to continue with the visualisation.
    """
    def __init__(self):

        with open ('simplemaps-worldcities-basic.csv', 'r') as f:
            csv_data = csv.DictReader(f)
            self.rows = list(csv_data)

    def get_coordinates(self, city):
        for i in self.rows:
            coordinates = []
            if city == i['city']:
                coordinates = [i['lat'], i['lng']]
                break
            else:
                coordinates = [0,0]
        return coordinates



def create_city_list():
    """
    Create a csv with all citys.
    """
    city_coordinates = CityCoordinates()
    companies_per_city = {}

    with open (CSV_FILE, 'r') as f:
        csv_data = csv.DictReader(f)
        rows = list(csv_data)

        # generate city list
        for i in rows:
            city = i['Stadt']
            if city not in companies_per_city:
                companies_per_city[city] = 1
        
        # count companies per city
        for i in rows:
            city = i['Stadt']
            if city in companies_per_city.keys():
                companies_per_city[city] += 1


        #write result in new csv file 
        fieldnames = ['Stadt','Anzahl_Firmen' ,'lat', 'lon']

        with open('city_list.csv', 'w') as new_f:

            # generate csv-file
            new_csv = csv.DictWriter(new_f, fieldnames=fieldnames)
            new_csv.writeheader()

            # write content
            for i in companies_per_city.keys():
                new_csv.writerow({'Stadt':i,'Anzahl_Firmen':companies_per_city[i], 'lat':city_coordinates.get_coordinates(i)[0], 'lon': city_coordinates.get_coordinates(i)[1]})




         


if __name__ == '__main__':
    create_city_list()
    



