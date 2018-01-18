#!/usr/bin/env python3
# Class that will become a utility to interact easier with json in python

import json
from pprint import pprint

class JsonUtils(object):
    """ Json utility library """

    def __init__(self):
        pass

    def decode(self, json_file):
        """ Decode a json string or file that contains json """

        with open(json_file, 'r') as f:
            data = json.load(f)
            return pprint(data)
