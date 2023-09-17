from bs4 import BeautifulSoup
import re
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) ' \
          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url = 'https://bama.ir/car?brand=tara,automatic,manual&year=,1402&price=100000000,10000000000&mileage=0&image=1&' \
      'priced=1&region=tehran,tehran&seller=1&color=white'
res = requests.get(url, headers= headers)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
val = soup.findAll('div', attrs={'class':"bama-ad-holder"})
print(val)