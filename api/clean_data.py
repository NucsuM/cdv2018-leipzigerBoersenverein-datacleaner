"""
Clean / expand the original data. Should be the basement for Roberts vue.js projekt.
Trying to clean as mutch data i can. Rest will be done by humans...
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

DATABASE = 'boersendaten.db'
TABLE = 'original_csv_data'
ORIGINAL_CSV_FILE = 'csv.csv'
    
    

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
        conn = sqlite3.connect(self.database)





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