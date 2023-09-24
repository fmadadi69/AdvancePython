import re
import time
import mysql.connector
from mysql.connector import errorcode
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


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
    cursor.execute("CREATE TABLE `cars_info`("
                   "`id` int NOT NULL AUTO_INCREMENT,"
                   "`vin` varchar(50) not null ,"
                   "`price` varchar(50) not null ,"
                   "`miles` varchar(50) not null ,"
                   "primary key (`id`)"
                   ")Engine = InnoDB")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print('Table already exists')


make = str(input('Enter name of car:(like kia-audi-fiat-ferrari-hyundai-maserati...)'))

browser = webdriver.Chrome()
browser.get(f'https://www.truecar.com/used-cars-for-sale/listings/{make}/')
# body = browser.find_element(By.TAG_NAME, 'body')

# no_pages = 10
# while no_pages:
#     body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
#     no_pages -= 1

# cars_info = browser.find_elements(By.XPATH, "//div[@data-test='usedListing']")
# for car in cars_info:
#     print(car.text)
# print(len(cars_info))

car_price = browser.find_elements(By.XPATH, "//span[@data-test='vehicleListingPriceAmount']")
# print([i.text for i in car_price])
# print(len(car_price))

car_miles = browser.find_elements(By.XPATH, "//div[@data-test='vehicleMileage']")
# print([j.text for j in car_miles])
# print(len(car_miles))

cars_vin = browser.find_elements(By.CLASS_NAME, 'vehicle-card-vin-carousel')
# print([k.text for k in cars_vin])
# print(len(cars_vin))

cars_info = zip(car_price, car_miles, cars_vin)
# cnx, cursor = configure_database()


query = f'INSERT INTO cars_info values ({cursor.lastrowid}, %(vin)s, %(price)s, %(miles)s)'
counter = 20


for price, miles, vin in cars_info:
    vin = re.findall(r'VIN\n([A-Za-z0-9]*)', vin.text)[0]
    # print(f"{price.text}, {miles.text}, {vin}")
    data = {
        'vin': vin,
        'price': price.text,
        'miles': miles.text}
    cursor.execute(query, data)
    cnx.commit()
    counter -= 1
    if counter < 1:
        break

cursor.close()
cnx.close()
browser.close()
