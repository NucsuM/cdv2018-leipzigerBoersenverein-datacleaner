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
# print some fancy dots
#print('.', sep=' ', end='', flush=True)



DATABASE = 'boersendaten.db'
TABLE = 'data'
CONN = sqlite3.connect(DATABASE)

COMPANY_TYPES = [
'Musikalienbuchhandlung',
'Verlagsbuchhandlung',
'Buchhandlung',
'Buchhandel',
'Verlag',
'Antiquariat',
'Verlagsbuchhandlung',
'Zeitschriftenhandlung',
'Buchverkaufsstelle', 
'Spielwarenhandlung', 
'Leihbücherei',
'Musikalien',
'Schreibwarenhandlung',
'Musikalienhandlung',
'Fotofachliteratur',
'Fachbuchhandlung',
'Fachantiquariat für Veterinärmedizin',
'Pianofortehandlung',
'Musikhaus',
'Buchbinderei',
'Fotofachliteratur',
'Schulbuchverkauf',
'Fachliteratur',
' Papier- und Schreibwaren']
    

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

    curser = CONN.cursor()
    curser.execute("""SELECT {} FROM {}""".format(columns, TABLE))
    rows = curser.fetchall()
    
    return rows


def compare_company_type(Aktentitel):
    """
    Return kind of company
    Logik muss kleverer werden!
    """
    company_type = [a for a in COMPANY_TYPES if a in Aktentitel]

    return company_type

def extract_city(Aktentitel):
    """
    Extract the City from the Aktentitel-column. Its in most cases the data
    after the last comma.
    Logik muss kleverer werden!
    """
    city = Aktentitel.split()[-1]

    return city


def add_column(name):
    """ 
    Add new column to db.
    """
    curser = CONN.cursor()
    #tpl = (TABLE, name, )
    
    try:
        curser.execute("""ALTER TABLE {} ADD COLUMN {} TEXT""".format(TABLE, name))
        CONN.commit()
    except Exception as e:
        logging.debug(e)
        pass


def main():
    "Expand sqlite-db with new columns"
    
    curser = CONN.cursor()
    data = read_data('Signatur, Aktentitel')
    
    add_column('Company')
    add_column('City')

    # add data for each signatur
    for i in data:
        company_type = compare_company_type(i[1])
        city = extract_city(i[1])
        signatur = i[0]
        
        tpl_company = (str(company_type), signatur)
        tpl_city = (str(city), signatur)

        curser.execute("""UPDATE data SET Company = ? WHERE SIGNATUR = ? """, tpl_company)
        curser.execute("""UPDATE data SET City = ? WHERE SIGNATUR = ? """, tpl_city)

    CONN.commit()

if __name__ == '__main__':    
    main()
    CONN.close()
