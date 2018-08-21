"""
Clean / expand the original data. Should be the basement for Roberts vue.js projekt.
Trying to clean as mutch data i can. Rest will be done by humans...

Fragen: 
1. Wie eine globale Config hinterlegen?
2. siehe get_spalten

"""
import logging
import sqlite3
import os.path
import sys

####################
# logging
####################

logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s: %(levelname)s  - "%(message)s" - f:%(funcName)s()')
logging.info('----------Logging started-------------')

####################



DATABASE = 'boersendaten.db'
TABLE = 'data'
COMPANY_TYPES = [
'Musikalienbuchhandlung',
'Verlagsbuchhandlung',
'Buchhandlung',
'Verlag',
'Antiquariat',
'Verlagsbuchhandlung'
]
    

def db_exists():
    """
    Check if db exists.
    """
    
    if os.path.exists(DATABASE):
        return True
    else:
        logging.error('{} Database not found'.format(DATABASE))
        sys.exit(0)


class CleanData:

    def __init__(self, database = DATABASE):
        self.database = database
        self.conn = sqlite3.connect(self.database)
        

    def get_spalten(self, spalten):
        "Select some coulmn date from the db"
        # TODO muss ich in einer Klassenfunktion hier self angeben?
        # s = spalte   # ist das notwendig?
        curser = self.conn.cursor()
        curser.execute("""SELECT {} FROM data""".format(spalten))
        rows = curser.fetchall()

        return rows

    def compare_company_type(self, Aktentitel):
        """Return kind of company"""

        for i in COMPANY_TYPES:
            if i in Aktentitel:
                return i

    def extract_company(self):
        "Get the company type from the column Aktentitel"
        column = 'Aktentitel' # überflüssig?
        title = self.get_spalten(column)

        for i in title:
            a = compare_company_type(i[0])
            print(a)




def main():
    """
    Import original csv date in slite-db.
    """ 

    if db_exists():
        conn = sqlite3.connect(DATABASE)

        # Insert new data
        conn.executemany('''INSERT INTO {} VALUES (?,?,?,?,?,?,?,?,?)'''.format(TABLE), rows[1:])
        conn.commit()
        conn.close()
        logging.info('New DB with original data created.')



if __name__ == '__main__':    
    main()