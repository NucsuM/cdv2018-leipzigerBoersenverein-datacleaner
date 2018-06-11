import csv

CSV_FILE = 'csv_new.csv'

def create_city_list():
    """
    Create a csv with all citys.
    """

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
        fieldnames = ['Stadt','Anzahl_Firmen' ,'lat', 'lan']

        with open('city_list.csv', 'w') as new_f:

            # generate csv-file
            new_csv = csv.DictWriter(new_f, fieldnames=fieldnames)
            new_csv.writeheader()

            # write content
            for i in companies_per_city.keys():
                new_csv.writerow({'Stadt':i,'Anzahl_Firmen':companies_per_city[i]})
            


if __name__ == '__main__':
    create_city_list()




