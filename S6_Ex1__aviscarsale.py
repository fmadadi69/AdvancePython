import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# def get_data(first_page, last_page):
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser.get(f"https://www.truecar.com/used-cars-for-sale/listings/location-columbia-md/?page=1")
# page_nums = browser.find_elements(By.XPATH, "//a[@data-test = 'paginationLink']")
# max_page = 0
# for i in page_nums:
#     if i.text.isdigit():
#         if int(i.text) > max_page:
#             max_page = int(i.text)
#
# if last_page > max_page:
#     return 'last_page is not valid'

# cars_info_list = []

# for page in range(1, 2):
cars_info_dict = dict()
browser.get(f"https://www.aviscarsales.com/used-inventory/index.htm?geoZip=&geoRadius=250")
# ?page={page}
body = browser.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.END)
time.sleep(0.2)
card_content = browser.find_elements(By.XPATH, "//div[@class = 'vehicle-card-details-container']")
for car in card_content:
    price = car.find_element(By.XPATH, ".//span[contains(@id, '_priceTitle')]")
    # cars_info_dict['price'] = price.text
    print(price.text)

    # make = car.find_element(By.XPATH, ".//span[@class = 'truncate']")
    # cars_info_dict['make'] = make.text
    #
    # price = car.find_element(By.XPATH, ".//span[@data-test = 'vehicleListingPriceAmount']")
    # cars_info_dict['price'] = price.text
    #
    # mileage = car.find_element(By.XPATH, ".//div[@data-test = 'vehicleMileage']")
    # cars_info_dict['mileage'] = mileage.text
    #
    # location = car.find_element(By.XPATH, ".//div[@data-test = 'vehicleCardLocation']")
    # cars_info_dict['location'] = location.text
    #
    # color = car.find_element(By.XPATH, ".//div[@data-test = 'vehicleCardColors']")
    # cars_info_dict['color'] = color.text
    #
    # condition = car.find_element(By.XPATH, ".//div[@data-test = 'vehicleCardCondition']")
    # cars_info_dict['condition'] = condition.text
    #
    # vin_general = car.find_element(By.XPATH, ".//div[contains(@class , 'vehicle-card-vin-carousel')]")
    # vin = re.findall(r'VIN\n([A-Za-z0-9]*)', vin_general.text)[0]
    # cars_info_dict['vin'] = vin

    # print(cars_info_dict)
    print("///////////////////////////////////////////////////////////////////")
    # cars_info_list.append(cars_info_dict)

# print(len(cars_info_list))
# return cars_info_list, datetime.datetime.now(), cars_info_list[0]['vin']
# print(cars_info_list)
# print(len(cars_info_list))

# print(get_data(1, 2))
