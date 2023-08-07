import requests
from bs4 import BeautifulSoup

url = "https://www.pythonscraping.com/pages/page3.html"
data = requests.get(url)

if data.status_code == 200:
    html = data.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)

else :
    print(data.status_code)

gifts = soup.select('#giftList > tr.gift')
# print(gifts)

for g in gifts:
    title = g.select('td')[0].text.strip()
    price = g.select('td')[2].text.strip()
    picture = g.select('td')[3].img['src']
    print(f"TITLE: {title}, PRICE: {price}")
    print(f"PIC: {picture}")