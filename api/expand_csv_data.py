"""
Convert csv data to an sqlite3 db.
"""
import logging
import sqlite3

####################
# logging
####################

logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s: %(levelname)s  - "%(message)s" - f:%(funcName)s()')
logging.info('----------Logging started-------------')

DATABASE = 'boersendaten.db'
ORIGINAL_TABLE = 'original_csv_data'
TABLE_COPY = 'working_copy'     


# connect db
try:
    conn = sqlite3.connect(DATABASE)

except sqlite3.OperationalError as e:
    logging.error(e)
    sys.exit(0)


def drop_table(table):
    try:
        conn.execute('''DROP TABLE {} '''.format(table))
        conn.commit()
    except:
        logging.info('{} did not exist - drop table skipped')


def create_table_copy():
    """
    Create sqlite-db copy.
    """
    drop_table(TABLE_COPY)
    
    conn.execute('''
        CREATE TABLE {}
        (Signatur TEXT,   
        DatumVon INT, 
        DatumBis INT, 
        Datierung Text, 
        Klassifikationsgruppe TEXT,  
        Aktentitel TEXT, 
        Vermerk TEXT, 
        Blattzahl TEXT, 
        Sortierfeld TEXT)'''.format(TABLE_COPY))

    logging.info('Table copy created.')
    
def _add_new_column(column, c_type):
    
    conn.execute(''' ALTER TABLE {} ADD COLUMN {} {}'''.format(TABLE_COPY, column, c_type))
    conn.commit()
    
    logging.info('Table erweitert')

def insert_data():
    pass__


def main():
    """
    Import original csv date in slite-db.
    """ 

    create_table_copy()
    _add_new_column('Stadt', 'TEXT')

if __name__ == '__main__':
    main()