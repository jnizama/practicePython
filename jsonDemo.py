import json
import urllib.request, urllib.parse, urllib.error

url = "https://py4e-data.dr-chuck.net/comments_2023422.json"
uh = urllib.request.urlopen(url)
url = uh.read().decode()
info = json.loads(url)


# print('User count:', len(info))
# print(json.dumps(info, indent=4))
# print(info["note"])
total = 0
for item in info["comments"]:
    #print('Name', item['count'])
    total = total + int(item['count'])
    # print('Id', item['id'])
    # print('Attribute', item['x'])
print(total)