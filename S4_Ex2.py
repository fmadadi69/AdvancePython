import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://divar.ir/s/tehran')
body = browser.find_element(By.TAG_NAME, 'body')

no_pages = 10
while no_pages:
    body.send_keys(Keys.END)
    time.sleep(0.2)
    no_pages -= 1

divar_Ads = browser.find_elements(By.CLASS_NAME, 'kt-post-card__description')
for ad in divar_Ads:
    print(ad.text)