import mysql.connector
from mysql.connector import errorcode

args = {'user': 'root', 'password': 'Baroon@5067082', 'host': '127.0.0.1'}
my_tables = dict()
my_tables['person'] = ('''CREATE TABLE `person`(
`id` int NOT NULL AUTO_INCREMENT,
`name` varchar(20) NOT NULL,
`weight` int NOT NULL,
`height` int NOT NULL,
PRIMARY KEY (`id`)
)Engine = InnoDB
''')

cnx = mysql.connector.connect(**args)
cursor = cnx.cursor()


def create_db(db_name):
    try:
        cursor.execute(f"create database {db_name} default character set 'UTF8MB4'")
    except mysql.connector.Error as err:
        print(f'Database failed to create due to {err.msg}')


def connect_db(db_name):
    try:
        cursor.execute(f'USE {db_name}')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            # print('Database not exists. Creating database...')
            create_db(db_name)
            # print(f'Database {db_name} created successfully')
            cnx.database = db_name


def create_tables(tables):
    for table_name, table_desc in tables.items():
        try:
            # print(f'Table {table_name}:', end=' ')
            cursor.execute(table_desc)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                # print('Already exists')
                pass
        # else:
            # print('ok')


def insert_data(table_name):
    insert_query = f'INSERT INTO {table_name} (id, name, weight, height) values (%(id)s, %(name)s, %(weight)s, %(height)s)'
    data = dict()
    data[1] = {
        'id': cursor.lastrowid,
        'name': 'Amin',
        'weight': 75,
        'height': 180
    }
    data[2] = {
        'id': cursor.lastrowid,
        'name': 'Mahdi',
        'weight': 90,
        'height': 190
    }
    data[3] = {
        'id': cursor.lastrowid,
        'name': 'Mohammad',
        'weight': 75,
        'height': 175
    }
    data[4] = {
        'id': cursor.lastrowid,
        'name': 'Ahmad',
        'weight': 60,
        'height': 175
    }
    for key, value in data.items():
        cursor.execute(insert_query, value)
        cnx.commit()


def read_data():
    data = []
    cursor.execute('SELECT * FROM person')
    for id, name, weight, height in cursor:
        # print(f'{id} {name} {weight} {height}')
        data.append({
            'name': name,
            'weight': weight,
            'height': height
        })
    data.sort(key=lambda e: e['weight'], reverse=False)
    data.sort(key=lambda e: e['height'], reverse=True)
    return data


def show_data(data):
    for d in data:
        print(f"{d['name']} {d['height']} {d['weight']}")


connect_db('advance_python')
create_tables(my_tables)
if not read_data():
    insert_data('person')
show_data(read_data())
