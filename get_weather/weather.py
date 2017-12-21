#!/usr/bin/env python
import json
import creds
import requests


class Weather(object):
    '''The Weather class which returns zipcode, city, city 5day, and city 16
    day forecasts.'''

    def __init__(self):
        self.temp_unit = '&units=imperial'
        self.base_url = 'http://api.openweathermap.org/data/2.5/'

    def zipcode(self, zip_code, country_code):
        r = requests.get(self.base_url + 'weather?zip=' + str(zip_code) + ','
                                                        + country_code
                                                        + self.temp_unit
                                                        + creds.api_login)
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def city_lookup(self, city_name, country_code):
        r = requests.get(self.base_url + 'weather?q=' + city_name + ','
                         + country_code
                         + self.temp_unit
                         + creds.api_login)
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def city_5d_fcast(self, city_name, country_code):
        r = requests.get(self.base_url + 'forecast?q=' + city_name + ','
                         + country_code
                         + self.temp_unit
                         + creds.api_login)
        return json.dumps(r.json(), sort_keys=True, indent=8)

    def city_16d_fcast(self, city_name, country_code, num_of_days):
        num_of_days = '&cnt=' + str(num_of_days)
        r = requests.get(self.base_url + 'forecast/daily?q=' + city_name + ','
                         + country_code
                         + self.temp_unit
                         + num_of_days
                         + creds.api_login)
        return json.dumps(r.json(), sort_keys=True, indent=4)


if __name__ == '__main__':
    weather = Weather()

    print(weather.city_lookup('Chicago', 'US'))
