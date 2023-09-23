import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# ####### For Windows #########
# browser = webdriver.Firefox()
browser = webdriver.Chrome(service=Service(r'C:\chromedriver\chromedriver.exe'))

# ####### For Mac #########
# browser = webdriver.Chrome()

browser.get('https://divar.ir/s/tehran/it-computer-jobs?payment_method=adaptive%2Cpercentage_commission')

body = browser.find_element(By.TAG_NAME, 'body')
no_pages = 10
while no_pages:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    no_pages -= 1


divar_Ads = browser.find_elements(By.CLASS_NAME, 'kt-post-card__body')

ads_list = []
print(divar_Ads)
for ad in divar_Ads:
    if ad.text.count('توافقی')>0:
        ads_list.append(ad.text)

for index in range(len(ads_list)):
    print(f'{index+1} : {ads_list[index]}\n')


browser.close()


# res = requests.get('https://divar.ir/s/tehran/rent-apartment')
# # print(res.text)
# soup = BeautifulSoup(res.text, 'html.parser')
# # # print(soup.prettify())
# # val = soup.findAll('div', attrs={'class':"kt-post-card__description"})
# # # val = soup.findAll('div', class_="kt-post-card__description")
# #
# # for v in val:
# #     print(v.text)
# a_str = soup.find(string='اجاره: توافقی')
# print(a_str)
# posts = a_str.find_parents('div', attrs={'class': "kt-post-card__body"})
# print(posts)
# for p in posts:
#     print(f'{p.text}\n')
