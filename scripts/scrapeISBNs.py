# scrapeISBNs.py
# Scrape wikipedia pages for ISBN numbers and return them as a list
# by Max Reinisch

import requests
# from readability import Document
from bs4 import BeautifulSoup
import re

# url = "https://en.wikipedia.org/wiki/Easter_Island"


# def striphtml(data):
#     p = re.compile(r'<.*?>')
#     return p.sub('', data)

# def request_wikipedia(url):
#     rec = requests.get(url)
#     if rec.status_code >=400:
#         print(status_code)
#         return None
#     doc = Document(rec.text)
#     return striphtml(doc.content())

def request_wikipedia(url):
    rec = requests.get(url)
    if rec.status_code >=400:
        print(status_code)
        return None
    soup = BeautifulSoup(rec.content, 'lxml')
    return soup.get_text()

def extractISBNs(article):
    isbn_identifier = re.compile(r"ISBN.[^A-Za-z]{9,}\d")
    isbns = isbn_identifier.findall(article)
    return [isbn[5:] for isbn in isbns]
    # return isbns

def getISBNs(url):
    article = request_wikipedia(url)
    if article:
        ISBNs = extractISBNs(article)
        return ISBNs
