# logging
import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s: %(levelname)s  - "%(message)s" - f:%(funcName)s()')
logging.info('----------Logging started-------------')

# original csv-file
ORIGINAL_CSV_FILE = 'csv.csv'

# sql-db settings
DATABASE = 'boersendaten.db'
TABLE = 'data'

# new columns
COMPANY_COLUMN = 'company'

# list of possible company-types
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