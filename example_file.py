import json

import requests


if __name__ == '__main__':
    url = 'http://localhost:2300/images/json'

    url_response: requests.models.Response = requests.get(url)

    images: list = json.loads(url_response.text)

    print('Используемые образы (images):')
    for image in images:
        print('\t', image.get('RepoTags')[0])


    url = 'http://localhost:2300/containers/json'

    url_response: requests.models.Response = requests.get(url)

    containers: list = json.loads(url_response.text)

    print('Контейнеры:')
    for container in containers:
        print(f'\t{container.get("Id")} - {container.get("Names")[0]} - {container.get("State")} - {container.get("Status")}')
        print(container.keys())

    url = 'http://localhost:2300/containers/fbda9a407f52/restart'

    # res = requests.post(url)
    #
    # print(res.status_code)
