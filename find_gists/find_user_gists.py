#!/usr/bin/env python3
# script to enumerate list of github users

import json
import requests
import sys


username = sys.argv[1]

def find_user_gists(username):
    r = requests.get(url='https://api.github.com/users/{}/gists'.format(username))
    json_data = json.loads(r.text)
    gist_urls = []
    for i in range(len(json_data)):
        gist_urls.append(json_data[i]['html_url'])
    return username, gist_urls


if __name__ == '__main__':
    user, urls = find_user_gists(username)
    print('Gists found for GitHub user: {} \n'.format(user))
    print('----------------------------------------------------------')
    for url in urls:
        print(url)
