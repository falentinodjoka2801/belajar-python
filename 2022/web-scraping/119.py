import requests, bs4, lxml

_response       =   requests.get('https://app.laukpauk.id/admin/auth/login')
_rawResponse    =   _response.text

_bs4                =   bs4.BeautifulSoup(_rawResponse, 'lxml')
_signInTextElement  =   _bs4.select('p.login-box-msg')[0]
_signInText     =   _signInTextElement.getText()

print(_signInText)