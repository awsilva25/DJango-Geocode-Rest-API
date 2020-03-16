from django.shortcuts import render
from distance.models import Distance
from distance.forms import LocationForm
import json


def IndexView(request):
    template_name = 'distance/index.html'
    form = LocationForm() # defined in forms.py
    return render(request, template_name, {'form': form})

def ResultsView(request):
    entered_origin = request.GET.get('origin')
    entered_destination = request.GET.get('destination')
    g = Distance(origin=entered_origin, destination=entered_destination)
    g.get_address_info()
    g.get_distance()
    g.save()

    # format data into a dictionary
    data = {
        "origin": {
            "entered_origin": g.origin,
            "origin_lat": g.origin_lat,
            "origin_long": g.origin_long,
            "full_origin_address": g.full_origin_address
        }, "destination": {
            "entered_destination": g.destination,
            "dest_lat": g.dest_lat,
            "dest_long": g.dest_long,
            "full_dest_address": g.full_dest_address
        }, "distance": g.calculated_distance
    }
    data = json.loads(json.dumps(data)) # convert dictionary to json
    context = {'data': data}
    return render(request, 'distance/results.html', context)


def MapsView(request):
    return render(request, 'distance/maps.html')
