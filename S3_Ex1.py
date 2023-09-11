import mysql.connector
from mysql.connector import errorcode

args = {'user': 'root', 'password': 'Baroon@5067082', 'host': '127.0.0.1'}
db_name = 'advance_python'
tables =dict()
tables['person'] = ('''CREATE TABLE `person`(
`id` int NOT NULL AUTO_INCREMENT,
`name` varchar(20) NOT NULL,
`weight` int NOT NULL,
`height` int NOT NULL,
PRIMARY KEY (`id`)
)Engine = InnoDB
''')

cnx = mysql.connector.connect(**args)
cursor = cnx.cursor()


def create_db(cursor, db_name):
    try:
        cursor.execute(f'CREATE DATABASE {db_name} DEFAULT CHARACTER SET "utf8"')
    except mysql.connector.Error as err:
        print(f'Database failed to create due to {err.msg}')


def connect_db(cursor, db_name):
    try:
        cursor.execute(f'USE {db_name}')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database not exists. Creating database...')
            create_db(cursor)
            print(f'Database {db_name} created successfully')
            cnx.database = db_name

def create_tables(tables):
    for table_name, table_desc in tables:
        print(f'database {}')
