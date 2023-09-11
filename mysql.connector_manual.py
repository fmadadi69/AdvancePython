import mysql.connector
from mysql.connector import errorcode

config = {'user': 'root', 'password': 'Baroon@5067082', 'host': '127.0.0.1',
          'raise_on_warnings': True, 'use_pure': 'False'}
db_name = 'advance_python'
tables = dict()
tables['person'] = (
    "CREATE TABLE `person` ("
    "`id` int NOT NULL AUTO_INCREMENT,"
    "`name` varchar(14),"
    "`age` int,"
    "`sex` varchar(1),"
    "PRIMARY KEY (`id`)"
    ")ENGINE = InnoDB")

tables['phone'] = ('''CREATE TABLE `phone`(
    `phone_id` int NOT NULL AUTO_INCREMENT
    ,`phone_number` varchar(11) NOT NULL
    ,`phone_type` enum('MOBILE', 'HOME') NOT NULL
    ,`person_id` int NOT NULL
    ,PRIMARY KEY (`phone_id`)
    ,CONSTRAINT fk1 FOREIGN KEY (`person_id`)
        REFERENCES `person` (`id`) ON DELETE CASCADE
    )ENGINE = InnoDB
    ''')


def create_db(cursor):
    try:
        cursor.execute(f'CREATE DATABASE {db_name} DEFAULT CHARACTER SET "utf8"')
    except mysql.connector.Error as err:
        print(f"Database failed to create: {err}")
        exit(1)


try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    try:
        cursor.execute(f'USE {db_name}')
    except mysql.connector.Error as err:
        print(f'Database {db_name} does not exist')
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_db(cursor)
            print(f"Database {db_name} created successfully")
        else:
            print(err.msg)
            exit(1)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Somthing wrong with username or password")
        cnx.database = db_name
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    for table_name, table_desc in tables.items():
        try:
            print(f'Creating table {table_name}: ', end=" ")
            cursor.execute(table_desc)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('Already exists')
            else:
                print(err)
        else:
            print('OK')
    add_person = (f"INSERT INTO person values (%(id)s, %(name)s, %(age)s, %(sex)s) ")
    data_person = {
        'id': cursor.lastrowid,
        'name': 'faezeh',
        'age': 33,
        'sex': 'F'}
    cursor.execute(add_person, data_person)

    add_phone = (f'INSERT INTO phone values ({cursor.lastrowid},"09125067082", "MOBILE", 1 )')
    cursor.execute(add_phone)
    cnx.commit()
    cursor.execute(f'SELECT * FROM person join phone on person.id = person_id')
    for (id, name, age, sex, phone_id, phone_number, phone_type, person_id) in cursor:
        print(f'{id} {name} {age} {phone_id} {phone_number} {phone_type}')
    cursor.close()
    cnx.close()
