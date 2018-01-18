#!/usr/bin/env python3
# Class that will become a utility to interact easier with json in python

import os
import json
from pprint import pprint

class JsonParser(object):
    """ Json utility library """
    def __init__(self):
        return


    def decode_file(self, json_file):
        """ Decode a json file """
        if os.path.isfile(json_file):
            with open(json_file, 'r') as f:
                data = json.load(f)
                return data


    def decode_str(self, json_str):
        """ Decode a json string """
        data = json.loads(json_str)
        return pprint(data)
