"""
Convert csv data to an sqlite3 db.
"""
import csv
import logging
import sqlite3
import os.path
import sys

####################
# logging
####################

logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s: %(levelname)s  - "%(message)s" - f:%(funcName)s()')
logging.info('----------Logging started-------------')

DATABASE = 'boersendaten.db'
TABLE = 'original_csv_data'
ORIGINAL_CSV_FILE = 'csv.csv'


def create_db():
    """
    Create sqlite-db.
    """

    # connect / create db
    try:
        conn = sqlite3.connect(DATABASE)
        # Drop Table
        try:
            conn.execute('''DROP TABLE {} '''.format(TABLE))
        except:
            pass
        conn.commit()
        
        conn.execute('''CREATE TABLE {}
             (Signatur TEXT,   DatumVon INT, DatumBis INT, Datierung Text, Klassifikationsgruppe TEXT,  
             Aktentitel TEXT, Vermerk TEXT, Blattzahl TEXT, Sortierfeld TEXT)'''.format(TABLE))
        conn.close()
        logging.info('New database created.')

    except sqlite3.OperationalError as e:
        logging.error(e)
        sys.exit(0)
    
    

def db_exists():
    """
    Check if db exists.
    """
    
    if os.path.exists(DATABASE):
        return True
    else:
        logging.error('Database not found')
        sys.exit(0)


def _get_original_csv_data():
    """
    Return csv data as list.
    """
    
    try:
        f = open(ORIGINAL_CSV_FILE, 'r')
    
    except FileNotFoundError:
        logging.error('File {} not found!'.format(ORIGINAL_CSV_FILE))
        sys.exit(0)

    csv_data = csv.reader(f)
    rows = list(csv_data)
    f.close()
    return rows


def main():
    """
    Import original csv date in slite-db.
    """ 

    create_db()

    rows = _get_original_csv_data()
    
    if db_exists():
        conn = sqlite3.connect(DATABASE)

        # Insert new data
        conn.executemany('''INSERT INTO {} VALUES (?,?,?,?,?,?,?,?,?)'''.format(TABLE), rows[1:])
        conn.commit()
        conn.close()
        logging.info('New DB with original data created.')



if __name__ == '__main__':    
    main()