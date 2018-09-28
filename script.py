import requests
WebinarsList = {}
workingId = 1538893
errorNum = 0
for id in range(1530000,1559999):
    url = 'https://events.webinar.ru/api/eventsessions/' + str(id) + '/record/isviewable?recordAccessToken=ajax'
    page = requests.get(url).json()
    if 'name' in page:
        WebinarsList[id] = page['name']
    else:
        if page['error']['code'] == 404:
            continue
        else:
            continue

for keys in WebinarsList:
    print(keys)
    print(WebinarsList[keys])

