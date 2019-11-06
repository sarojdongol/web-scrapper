from bs4 import  BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import argparse
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()

parser = argparse.ArgumentParser(description='Web Scrapper Arguments!')
parser.add_argument("--U", help="Target website URL")

def WebScrapyer(url):
    try:
        html = urlopen(url,context=context)
        if(html is None):
            return "URL not found"
        else:
            bsObj = BeautifulSoup(html,'html.parser')
            content_lis = bsObj.find_all('div', {'class': 'sydney-cruise-left tab-group'})
            return content_lis
            

    except (AttributeError,HTTPError) as err:
        print("Please provide correct  website url",err)

if  __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Web Scrapper Arguments!')
    parser.add_argument("--U", help="Target website URL")
    ##adding url as a arugment
    args = parser.parse_args()
    url = args.U
    print(WebScrapyer(url))
