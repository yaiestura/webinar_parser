import requests

webinar_list = {}
workingId = 1538893

id = 1550050
idk = 1547155
errorNum = 0

while (id < 1550060) & (id >= 1550060):
    url = 'https://events.webinar.ru/api/eventsessions/' + str(int(id)) + '/record/isviewable?recordAccessToken=ajax'
    response = requests.get(url)
    if response.status_code == 404:
        id += 1
        continue
    else:
        webinar_list[id] = response.json()['name']
        id += 1

for keys in webinar_list:
    print(keys)
    print(webinar_list[keys])