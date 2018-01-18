#!/usr/bin/env python3
# Class that will become a utility to interact easier with json in python

import os
import json
from pprint import pprint

class JsonUtils(object):
    """ Json utility library """


    def decode(self, json_file):
        """ Decode a json string or file that contains json """
        if os.path.isfile(json_file):
            with open(json_file, 'r'):
                data = json.load(json_file)
                return pprint(data)
        else:
            data = json.loads(json_file)
            return pprint(data)
