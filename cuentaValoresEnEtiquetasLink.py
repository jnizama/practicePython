# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
nombreFinal = ''
contador = 1
for tag in tags:
    if contador = 18:
        html2 = urlopen(tag.get('href', None), context=ctx).read()
        soup2 = BeautifulSoup(html2, "html.parser")
        tags2 = soup('a')
        for i in range(1,7):
            contador2 = 1
            for tag2 in tags2:                
                if i == 17:
                    nombreFinal = tag2

    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    contador = contador + 1
    
