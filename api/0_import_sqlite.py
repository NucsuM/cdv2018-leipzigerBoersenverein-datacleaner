"""
Convert csv data to an sqlite3 db.
Ist eigentlich komplett überflüssig, da der Import komplett über sqlite3 gehen kann. Später..
"""
import csv
import logging
import sqlite3
import os.path
import sys
from settings import *


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

        # Insert new data and add new columns
        conn.executemany('''INSERT INTO {} VALUES (?,?,?,?,?,?,?,?,?)'''.format(TABLE), rows[1:])
        conn.commit()
        conn.close()
        logging.info('New DB with original data created.')



if __name__ == '__main__':    
    main()