from bs4 import  BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import argparse
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()

##Defining class to crawl
'''Below "product-container gives all the datasets including dinner"'''
dinner_main_holder = "child-navs tab-cnt hide dinner-tab"
dinner_container_class = 'product-container'


def WebScrapyer(url):
    try:
        html = urlopen(url,context=context)
        if(html is None):
            return "URL not found"
        else:
            bsObj = BeautifulSoup(html,'html.parser')
            ul  =  bsObj.find('li', class_ = dinner_main_holder)
            dinner = ul.li
            for item in dinner:
                try:
                        description = item.find(class_='cruise-text-box').text
                        full_price = item.find(class_="full-price").text
                        actual_price = item.find(class_='actual').text
                        child_price = item.find(class_='other-price').text
                        save_price = item.find(class_='save-price-amount').text
                        print(description,full_price, actual_price,child_price, save_price)
                except :
                        pass


    except (AttributeError,HTTPError) as err:
        print("Please provide correct  website url",err)

if  __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Web Scrapper Arguments!')
    parser.add_argument("--U", help="Target website URL")
    ##adding url as a arugment
    args = parser.parse_args()
    url = args.U
    print(WebScrapyer(url))
