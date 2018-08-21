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
'Buchhandlung'
'Buchhandel',
'Verlag',
'Antiquariat',
'Verlagsbuchhandlung',
'Zeitschriftenhandlung',
'Buchverkaufsstelle', 
'Spielwarenhandlung'  ]
    

def db_exists():
    """
    Check if db exists.
    """
    
    if os.path.exists(DATABASE):
        return True
    else:
        logging.error('{} Database not found'.format(DATABASE))
        sys.exit(0)


def read_data(columns):
    """
    Select some coulmn date from the db.
    Return list with rows    
    """
    # s = spalte   
    #database = DATABASE # ist das notwendig?
    #table = TABLE

    conn = sqlite3.connect(DATABASE)
    curser = conn.cursor()
    curser.execute("""SELECT {} FROM {}""".format(columns, TABLE))
    rows = curser.fetchall()
    conn.close()
    
    return rows


def compare_company_type(Aktentitel):
    """
    Return kind of company
    Logik muss kleverer werden!
    """
    company_type = [a for a in COMPANY_TYPES if a in Aktentitel]

    return company_type

def add_column(name):
    """ 
    Add new column to db.
    """

    conn = sqlite3.connect(DATABASE)
    curser = conn.cursor()
    tpl = (TABLE, name)
    
    try:
        curser.execute("""ALTER TABLE ? ADD COLUMN ? TEXT""", tlp)
    except:
        pass

    conn.close()


def add_company():
    "Expand sqlite-db with company type from column Aktentitel"
    
    conn = sqlite3.connect(DATABASE)
    curser = conn.cursor()
    data = read_data('Signatur, Aktentitel')
    
    add_column('Company')

    # add company to new column
    for i in data:
        company_type = compare_company_type(i[1])
        signatur = i[0]
        tpl = (str(company_type), signatur)
        
        curser.execute("""UPDATE data SET Company = ? WHERE SIGNATUR = ? """, tpl)
        print('.', sep=' ', end='', flush=True)
        
    conn.commit()
    conn.close()


if __name__ == '__main__':    
    add_company()
    #read_data('Signatur, Aktentitel')