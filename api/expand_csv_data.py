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
ORIGINAL_TABLE = 'original_csv_data'
TABLE_COPY = 'working_copy'     

def create_table_copy():
    """
    Create sqlite-db copy.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        # Drop Table
        conn.execute('''DROP TABLE {} '''.format(TABLE_COPY))
        conn.commit()
        
        conn.execute('''CREATE TABLE {}
             (Signatur TEXT,   DatumVon INT, DatumBis INT, Datierung Text, Klassifikationsgruppe TEXT,  
             Aktentitel TEXT, Vermerk TEXT, Blattzahl TEXT, Sortierfeld TEXT)'''.format(TABLE_COPY))
        conn.close()
        logging.info('Table copy created.')

    except sqlite3.OperationalError as e:
        logging.error(e)
        sys.exit(0)
    
def _add_new_column(column, c_type):
    column = column
    c_type = c_type
    conn = sqlite3.connect(DATABASE)
    conn.execute(''' ALTER TABLE {} ADD COLUMN {} {}'''.format(TABLE_COPY, column, c_type))
    conn.commit()
    conn.close()
    logging.info('Table erweitert')


def main():
    """
    Import original csv date in slite-db.
    """ 

    create_table_copy()
    _add_new_column('Stadt', 'TEXT')', 'TEXT')



if __name__ == '__main__':
    main()