#! python3

# checks sites and send an email if price has changed

import requests, bs4, ezgmail, threading, subprocess

url1 = 'https://www.chainreactioncycles.com/sk/en/brand-x-ascend-cx-dropper-seatpost-85-105mm-/rp-prod159175'
price1 = '153.99'

url2 = 'https://www.wiggle.co.uk/brand-x-ascend-cx-dropper-seatpost-85-105mm'
price2 = '€156.29'


email = ''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'}

def sitecheck1(url, price):
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    priceCheck = soup.select('.crcPDPPriceHidden')
    currentPrice = priceCheck[0].getText().strip()

    if currentPrice != price:
        ezgmail.send(email, 'Zmena ceny!', '%s' %url)
        subprocess.Popen(['start', 'chainreactioncycle.txt'], shell=True)
        

def sitecheck2(url, price):
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    priceCheck = soup.select('.bem-pricing > p')
    currentPrice = priceCheck[0].getText().strip()

    if currentPrice != price:
        ezgmail.send(email, 'Zmena ceny!', '%s' %url)
        subprocess.Popen(['start', 'wiggle.txt'], shell=True)


threadObj = threading.Thread(target=sitecheck1, args=[url1,price1])
threadObj.start()

threadObj2 = threading.Thread(target=sitecheck2, args=[url2,price2])
threadObj2.start()

