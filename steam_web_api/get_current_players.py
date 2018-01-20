#!/usr/bin/env python3
""" Queries Steam API for number of current players playing in all Steam
games.
"""

import json
import requests

BASE_URL = 'https://api.steampowered.com'


def main():
    """ Loop through list of appids and feed appid list into retrieval of
    current players in game corresponding to appid
    """

    appnames, appids = zip(*get_appid())

    for appname, appid in zip(appnames, appids):
        resp_data = json.loads(get_current_players(appid))
        player_count = resp_data['response']['player_count']
        print('Game Name: {}'.format(appname))
        print('Current Players: {}\n'.format(player_count))


def get_current_players(appid):
    """ Queries Steam API for number of current players  in a game

    :param appid: The appid of the game title
    :param type: `str`
    
    :returns: Returns string json response of number of current players
    :rtype: `str`
    """

    url = '{}/ISteamUserStats/GetNumberofCurrentPlayers/v1/?key=KEY&format=json&appid={}'.format(BASE_URL, appid)
    r = requests.get(url)
    return r.text


def get_appid():
    """ Queries Steam API for appids
    :returns: (appname, appid)
    :rtype: `tuple`
    """
    url = '{}/ISteamApps/GetAppList/v2'.format(BASE_URL)
    r = requests.get(url)
    json_data = json.loads(r.text)
    apps = json_data['applist']['apps']
    appname_and_id = [(dic['name'], dic['appid']) for dic in apps]

    return appname_and_id


if __name__ == '__main__':
    main()
