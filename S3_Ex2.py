import re
import mysql.connector
from mysql.connector import errorcode


def check_username_format(myuser):
    p = re.compile('[A-Za-z-0-9]+\@[A-Za-z]+\.[A-Za-z]+')
    m = p.match(myuser)
    if m is None:
        return False
    elif m.group() != myuser:
        return False
    elif m.group() == myuser:
        return True


def check_password_format(mypass):
    p = re.compile('[A-Za-z0-9]+')
    m = p.match(mypass)
    if m is None:
        return False
    elif m.group() != mypass:
        return False
    elif m.group() == mypass:
        return True


# print(check_username_format(input()))


def get_input():
    username = str(input())
    while not check_username_format(username):
        print('Email format is not correct. It should be like: "expression@string.string" ')
        username = str(input())

    password = str(input())
    while not check_password_format(password):
        print('Password just includes string and number')
        password = str(input())

    return username, password


def create_database(db_name):
    try:
        cursor.execute(f"CREATE DATABASE {db_name} DEFAULT CHARACTER SET 'utf8' ")
    except mysql.connector.Error as err:
        print(f'Failed to create database because {err}')
        exit(1)


def make_db_connection(db_name):
    try:
        cursor.execute(f'USE {db_name}')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database not Exist.Creating database...')
            create_database(db_name)
            print('Database created')
            cnx.database = db_name
        else:
            print(err)
            exit(1)


def create_table(table):
    try:
        cursor.execute(table[1])
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Table already exists')
        else:
            print(err.msg)


def insert_data(table, user, password):
    data = {
        'id': cursor.lastrowid,
        'username': user,
        'password': password
    }
    query = f'INSERT INTO {table}  VALUES (%(id)s,%(username)s,%(password)s)'
    cursor.execute(query, data)
    cnx.commit()


def show_data():
    print("Table USER contains:")
    cursor.execute("SELECT * FROM user")
    for id, username, password in cursor:
        print(f"{id}  {username}  {password}")


config = {'user': 'root', 'password': 'Baroon@5067082', 'host': '127.0.0.1'}
mytable = ('user', (f"""CREATE TABLE `user` (
    `id` int NOT NULL AUTO_INCREMENT,
    `username` varchar(50) NOT NULL ,
    `password` varchar(50) NOT NULL ,
    PRIMARY KEY (`id`)
)ENGINE = InnoDB"""))


email, passw = get_input()
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
make_db_connection('AdvancePython')
create_table(mytable)
insert_data(mytable[0], email, passw)
show_data()
cursor.close()
cnx.close()
