
from .logic.logic_measurements import get_all_measurements, get_measurement_by_pk
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type = 'application/json')

def get_measurement(request, measurement_id):
    return HttpResponse(serializers.serialize('json', get_measurement_by_pk(measurement_id)), content_type = 'application/json')
