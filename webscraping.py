import time

from bs4 import BeautifulSoup
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from fake_useragent import UserAgent
# from pyvirtualdisplay import Display
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#
# display = Display(visible=0, size=(1920, 1080))
# display.start()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url = 'https://bama.ir/car?brand=tara,automatic,manual&year=,1402&price=100000000,10000000000&mileage=0&image=1&priced=1&region=tehran,tehran&seller=1&color=white'
# res = requests.get(url, headers= headers)
# # print(res.text)
#
# soup = BeautifulSoup(res.text, 'html.parser')
# # print(soup)
# val = soup.findAll('div', attrs={'class':"bama-ad-holder"})
# print(val)


ua = UserAgent()
user_agent = ua.chrome
opts = Options()
opts.page_load_strategy = 'normal'
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")
opts.add_argument(f'user-agent={user_agent}')
opts.add_argument("--js-flags=--harmony")
opts.add_argument("driver_path=C:\chromedriver\chromedriver.exe")
browser = webdriver.Chrome(options=opts)
browser.get(url)
time.sleep(1)

element = browser.find_element(By.TAG_NAME, 'body')

no_of_page_downs = 20

while no_of_page_downs:
    element.send_keys(Keys.END)
    time.sleep(0.2)
    no_of_page_downs -= 1


cars_info = browser.find_elements(By.CLASS_NAME, "bama-ad-holder")

for car in cars_info:
    print(car.text)

