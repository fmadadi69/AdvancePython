import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

# def get_data(first_page, last_page):
# browser = uc.Chrome()
opts = uc.ChromeOptions()
opts.add_argument('--headless=new')
opts.add_argument('ignore-certificate-errors')
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--remote-allow-origins=*")
browser = uc.Chrome(browser_executable_path='chromedriver.exe')
# options=opts, executable_path = './chromedriver.exe')
browser.maximize_window()
time.sleep(10)
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
browser.get(f"https://www.carsdirect.com/used_cars/listings?zipcode=90245&dealerId=&distance=50&yearFrom=&yearTo"
            f"=&priceFrom=&priceTo=&qString=&keywords=&makeName=&modelName=&sortColumn=&sortDirection=&searchGroupId"
            f"=&lnk=&recentSearchId=14611883&initialSearch=false&pageNum=1")
# ?page={page}

card_content = browser.find_elements(By.XPATH, "//div[@class = 'list-details']")
for car in card_content:
    name = car.find_element(By.XPATH, ".//span[@itemprop = 'name']")
    cars_info_dict['year'] = name.text

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

    print(cars_info_dict)
    print("///////////////////////////////////////////////////////////////////")
    # cars_info_list.append(cars_info_dict)

# print(len(cars_info_list))
# return cars_info_list, datetime.datetime.now(), cars_info_list[0]['vin']
# print(cars_info_list)
# print(len(cars_info_list))

# print(get_data(1, 2))
