import requests
import os

webinar_list = {}
workingId = 1538893

id = workingId

if not os.path.isfile('urls.txt'):
    with open('urls.txt', 'w') as f:
        f.write("")

while (id < 1600000):
    id += 1
    url = 'https://events.webinar.ru/api/eventsessions/' + str(int(id)) + '/record/isviewable?recordAccessToken=ajax'

    try:
        response = requests.get(url)
    except Exception as e:
        id -= 1

    if response.status_code != 404:
        try:
            webinar_list[id] = response.json()['name']
        except Exception as e:
            pass

        with open('urls.txt', 'a') as f:
            video_url = "https://events.webinar.ru/{user_id}/{event_id}/record-new/{id}".format(
                user_id=str(response.json()['createUser']['id']),
                event_id=str(response.json()['event']['id']),
                id=str(id))
            webinar_name = response.json()['name']

            f.write(webinar_name + '\n')
            f.write(video_url + '\n')
