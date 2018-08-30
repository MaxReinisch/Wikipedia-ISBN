import requests
from scrapeISBNs import getISBNs
from bs4 import BeautifulSoup
import json



def getIdentifier(isbn):
    qurl = f'https://archive.org/advancedsearch.php?q={isbn}&fl%5B%5D=identifier&sort%5B%5D=&sort%5B%5D=&sort%5B%5D=&rows=50&page=1&output=json&callback=callback&save=yes#raw'
    res = requests.get(qurl)
    if res.status_code >=400:
        return None
    json_res = json.loads(res.text[9:-1])
    if json_res['response']['numFound'] == 0:
        return None
    if json_res['response']['numFound'] >1:
        print("More than one response")
    return json_res['response']['docs'][0]['identifier']

def getBookInfo(identifier):
    qurl = f'https://archive.org/metadata/{identifier}'
    res = requests.get(qurl)
    if res.status_code >= 400:
        return None
    json_res = json.loads(res.text)
    return json_res['metadata']

def main():
    url = "https://en.wikipedia.org/wiki/Easter_Island"
    ISBNs = getISBNs(url)
    for ISBN in ISBNs:
    # ISBN = ISBNs[0]
        identifier = getIdentifier(ISBN)

        if identifier:
            print(identifier)
            print(f"https://archive.org/services/img/{identifier}")
            print(f"https://archive.org/details/{identifier}")
            print()
    #     bookInfo = getBookInfo(identifier)
    #     print(bookInfo)


main()
