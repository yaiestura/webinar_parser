import requests
id = 1547159
url = 'https://events.webinar.ru/api/eventsessions/' + str(id) + '/record/isviewable?recordAccessToken=ajax'
page = requests.get(url).json()
print(page)