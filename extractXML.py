import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://py4e-data.dr-chuck.net/comments_2023421.xml '


    #address = input('Enter location: ')
    #if len(address) < 1: break

    
    #url = serviceurl + urllib.parse.urlencode({'address': 'http://py4e-data.dr-chuck.net/comments_42.xml'})
    #print('Retrieving', url)
uh = urllib.request.urlopen(serviceurl)
data = uh.read()
print('Retrieved', len(data), 'characters')
    #print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments')[0]
#r1 = results.find('comment').text
total = 0
for r in results:
    result = int(r.find('count').text)
    total = total + result
print(total)
#lat = results[0].find('comment').find('name').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text

