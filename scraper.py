import request
from bs4 import BeautifulSoup

URL = 'https://www.amazon.de/RAVPower-Alpha7-Ersatzakkus-1100mAh-USB-Input/dp/B06WD8W4PB/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=V9Q30LZVIGIB&keywords=sony+alpha+7&qid=1578442495&s=ce-de&sprefix=sony+a%2Celectronics%2C254&sr=1-1-spons&psc=1&smid=A2X2NO3429IQ5W&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyM01WWURURkRHSjRQJmVuY3J5cHRlZElkPUEwMzM3NTc4MVRIRFJLMkNFQ00wQiZlbmNyeXB0ZWRBZElkPUEwOTAxMTE0WkJUU040TVJCN0NMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers =  {
     "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}   
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")

print(title)
