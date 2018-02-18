# import the libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# specify the url
quote_page=['https://www.bloomberg.com/quote/SPX:IND']
data=[]
for pg in quote_page:
    # query the website and return the html to the variable 'page'
    page = urllib2.urlopen(pg)

    # parse the html using bf soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('h1', attrs={'class': 'name'})

    # strip is used to remove starting and trailing
    name = name_box.text.strip()

    print name

    # to get the price
    price_box = soup.find('div', attrs={'class': 'price'})
    price = price_box.text.strip()
    print price

    # open_box=soup.find('div', attrs={'class':'cell__value cell__value_'})
    # openPrice=open_box.text.strip()
    # print openPrice




    data.append((name, price,openPrice))



# open a csv file with append, so old data will not be srased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for name,price,openPrice in data:
        writer.writerow([name, price,openPrice, datetime.now()])







