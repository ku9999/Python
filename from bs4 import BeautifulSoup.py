import requests
from bs4 import BeautifulSoup
url='https://itorrents-igruha.org/repack-by-igruha/'
req=requests.get(url)
src=req.text
print(src)