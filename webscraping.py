import time

import mysql.connector
from bs4 import BeautifulSoup
import re
import requests
from mysql.connector import errorcode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

from fake_user_agent import user_agent
from selenium.webdriver.firefox.service import Service
from webdrivermanager.chrome import ChromeDriverManager

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
#                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url = 'https://bama.ir/car?brand=tara,automatic,manual&year=,1402&price=100000000,10000000000&mileage=0&image=1&priced=1&region=tehran,tehran&seller=1&color=white'


# res = requests.get(url, headers= headers)
# # print(res.text)
#
# soup = BeautifulSoup(res.text, 'html.parser')
# # print(soup)
# val = soup.findAll('div', attrs={'class':"bama-ad-holder"})
# print(val)


def config_database():
    args = {'user': 'root', 'password': 'Baroon@5067082', 'host': '127.0.0.1'}
    db_name = 'Advance_Python'
    cnx = mysql.connector.connect(**args)
    cursor = cnx.cursor()
    try:
        cursor.execute(f'USE {db_name}')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            cursor.execute(f'CREATE DATABASE {db_name} default character set "utf8"')
            cnx.database = db_name
    try:
        cursor.execute(f'CREATE TABLE `car` ('
                       f'`id` int not null auto_increment,'
                       f'`model` varchar(50),'
                       f'`date_of_advertise` varchar(50),'
                       f'`year` varchar(50),'
                       f'`karkard` varchar(50),'
                       f'`gearbox` varchar(50),'
                       f'`address` varchar(50),'
                       f'`price` varchar(50),'
                       f'primary key (`id`)'
                       f')Engine = InnoDB')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Table Exists')
        else:
            print(err)
    return cnx, cursor


# ua = user_agent()
opts = webdriver.ChromeOptions()
opts.page_load_strategy = 'normal'
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")
# opts.add_argument(f'user-agent={ua}')
opts.add_argument("--js-flags=--harmony")
# opts.add_argument("driver_path=/usr/local/bin/chromedriver")
browser = webdriver.Chrome(options=opts)
# browser = webdriver.Firefox()
browser.get(url)
time.sleep(1)

element = browser.find_element(By.TAG_NAME, 'body')

no_of_page_downs = 20

while no_of_page_downs:
    element.send_keys(Keys.END)
    time.sleep(0.2)
    no_of_page_downs -= 1

cars_info = browser.find_elements(By.CLASS_NAME, "bama-ad-holder")
car_dict = {'model': '', 'date_of_advertise': '', 'year': '', 'karkard': '', 'gearbox': '', 'address': '', 'price': ''}
car_list = []
cnx, cursor = config_database()
for car in cars_info:
    # print(re.sub(r'\s+', ' ', car.text).strip())
    car_list = car.text.split('\n')
    for key, i in zip(car_dict.keys(), range(len(car_dict))):
        car_dict[key] = car_list[i]
    query = f'INSERT INTO car values (%(id)s, %(model)s, %(date_of_advertise)s, %(year_of_creation)s, %(karkard)s, %(gearbox)s, %(address)s, %(price)s)'
    data = {
        'id': cursor.lastrowid+1,
        'model': car_dict['model'],
        'date_of_advertise': car_dict['date_of_advertise'],
        'year_of_creation': car_dict['year'],
        'karkard': car_dict['karkard'],
        'gearbox': car_dict['gearbox'],
        'address': car_dict['address'],
        'price': car_dict['price']
    }
    cursor.execute(query, data)
    cnx.commit()

    # print(car_dict)

cursor.execute('SELECT * FROM car')
for id, model, date_of_ad, year,karkard,gearbox, address, price in cursor:
    print(f'{id}:  {model}, {date_of_ad}, {year}, {karkard}, {gearbox}, {address}, {price}')

cnx.close()

browser.quit()
