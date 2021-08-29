
from .logic.logic_measurements import get_all_measurements, get_measurement_by_pk
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type = 'application/json')

def get_measurement(request, measurement_id):
    measurement = get_measurement_by_pk(measurement_id)
    measurement_s = serializers.serialize('json',measurement)
    return HttpResponse(measurement_s, content_type = 'application/json')
