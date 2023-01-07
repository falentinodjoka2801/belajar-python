_result     =   requests.get('http://www.example.com')
_htmlResut  =   _result.text

_soup   =   bs4.BeautifulSoup(_htmlResut, 'lxml')
print(_soup)