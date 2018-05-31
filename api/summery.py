import csv

CSV_FILE = 'csv_new.csv'

def create_city_list():
    """
    Create a csv with all citys and the number of companies
    """
    city_list=[]

    with open (CSV_FILE, 'r') as f:
        csv_data = csv.DictReader(f)
        rows = list(csv_data)

        # generate city list
        for i in rows:
            if i['Stadt'] not in city_list:
                city_list.append(i['Stadt'])
        

        #crate a new csv_file 
        fieldnames = ['Stadt', 'Koordinaten', 'Anzahl Firmen']

        with open('city_list.csv', 'w') as new_f:

            # generate file
            new_csv = csv.DictWriter(new_f, fieldnames=fieldnames)
            new_csv.writeheader()

            # write cities
            for i in city_list:
                new_csv.writerow({'Stadt':i})
            
            # write amount of companies

            for i in rows:



if __name__ == '__main__':
    create_city_list()