import requests
from bs4 import BeautifulSoup

url = 'http://www.amazon.in/s'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}

product = 'amazon alexa'

def match(description, text):
    l = text.split(' ')
    ctr = 0
    for i in range(len(l)):
        if l[i] in description:
            ctr = ctr + 1
    if ctr/len(l) < 0.65:
        return False
    else:
        return True


params = {'field-keywords':product}

def magic():
    r = requests.get(url, params = params, headers = headers)

    if r.status_code == 200:
        print(r.url)
        soup = BeautifulSoup(r.text, 'lxml')
        div = soup.find(id = 'atfResults')
        items = div.find_all('li')
        res = []
        for item in items:
            heading = item.h2.text
            priceText = item.find(class_ = 's-price').text
            price = priceText.replace('\xa0', '')
            price = price.replace(',', '')
            price = float(price)
            print(price)
            if match(heading.lower(), product.lower()):
                res.append(price)

        if len(res) > 0:
            res.sort()
            print('Result', res[0])
            print(res)
        else:
            print('NO Result')


if __name__ == '__main__':
    magic()

