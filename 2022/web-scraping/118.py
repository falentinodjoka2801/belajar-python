import requests, bs4

_url    =   'http://www.example.com'
_result =   requests.get(_url)
_resultText =   _result.text

_bs =   bs4.BeautifulSoup(_resultText, "lxml")

_pageTitleElement  =   _bs.select('title')
_pageTitle  =   _pageTitleElement[0].getText()
print(_pageTitle)