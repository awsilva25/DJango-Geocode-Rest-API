from django.db import models
from math import sin, cos, sqrt, atan2, radians
import urllib.request
import json

API_KEY = ''
endpoint = 'https://maps.googleapis.com/maps/api/geocode/json?'

class Distance(models.Model):
    origin = models.CharField(max_length=250, null=True)
    origin_lat = models.DecimalField(max_digits=30, decimal_places=20, null=True)
    origin_long = models.DecimalField(max_digits=30, decimal_places=20, null=True)
    full_origin_address = models.CharField(max_length=250, null=True)

    destination = models.CharField(max_length=250, null=True)
    dest_lat = models.DecimalField(max_digits=30, decimal_places=20, null=True)
    dest_long = models.DecimalField(max_digits=30, decimal_places=20, null=True)
    full_dest_address = models.CharField(max_length=250, null=True)

    calculated_distance = models.DecimalField(max_digits=30, decimal_places=2, null=True)

    def get_address_info(self):
        # send google maps geocode api request for user origin input and retrieve data into json format
        origin_address = self.origin.replace(' ','+')
        origin_nav_request = 'address={}&key={}'.format(origin_address, API_KEY)
        origin_request = endpoint + origin_nav_request
        origin_response = urllib.request.urlopen(origin_request).read()
        origin_data = json.loads(origin_response)
        if (origin_data['status']=="ZERO_RESULTS"):
            self.origin_lat = None
            self.full_origin_address = 'Address or place "{}" not found.'.format(self.origin)
        else:
            origin_coords = origin_data['results'][0]['geometry']['location']
            self.origin_lat = origin_coords['lat']
            self.origin_long = origin_coords['lng']
            self.full_origin_address = origin_data['results'][0]['formatted_address']

        # send google maps geocode api request for user destination input and retrieve data into json format
        dest_address = self.destination.replace(' ','+')
        dest_nav_request = 'address={}&key={}'.format(dest_address, API_KEY)
        dest_request = endpoint + dest_nav_request
        dest_response = urllib.request.urlopen(dest_request).read()
        dest_data = json.loads(dest_response)
        if (dest_data['status']=="ZERO_RESULTS"):
            self.dest_lat = None
            self.full_dest_address = 'Address or place "{}" not found.'.format(self.destination)
        else:
            dest_coords = dest_data['results'][0]['geometry']['location']
            self.dest_lat = dest_coords['lat']
            self.dest_long = dest_coords['lng']
            self.full_dest_address = dest_data['results'][0]['formatted_address']

    # function to calculate distance between origin and destination
    def get_distance(self):
        # case place or address not found with geocode api for inputted data
        if self.origin_lat==None or self.dest_lat==None:
            self.calculated_distance=None
            return

        radius = 6371000 # in meters
        phi_1 = radians(self.origin_lat)
        phi_2 = radians(self.dest_lat)
        delta_phi = radians(self.dest_lat-self.origin_lat)
        delta_lambda = radians(self.dest_long-self.origin_long)

        a = sin(delta_phi / 2)**2 + cos(phi_1) * cos(phi_2) * sin(delta_lambda / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))

        calc_distance = (radius*c) # distance in meters
        calc_distance *= 0.621371/1000 # convert to miles

        self.calculated_distance = round(calc_distance, 2)
