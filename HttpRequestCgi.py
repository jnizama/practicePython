import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.bullionvault.com/secure/j_security_check?j_username=JNIZAMA&j_password=Bethel2521')
soup = BeautifulSoup(r.text)
metas = soup.find_all('meta')

print(metas)

