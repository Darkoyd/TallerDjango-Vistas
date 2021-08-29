
from .logic.logic_measurements import get_all_measurements, get_measurement_by_pk, delete_measurement_by_pk, update_measurement_value
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type = 'application/json')


def get_measurement(request, measurement_id):
    measurement = get_measurement_by_pk(measurement_id)
    return HttpResponse(measurement, content_type = 'application/json')

def delete_measurement(request, measurement_id):
    delete_measurement_by_pk(measurement_id)
    return HttpResponse(str(measurement_id) + ' deleted')

def update_measurement(request, measurement_id, new_value):
    measurement = update_measurement_value(measurement_id, new_value)
    return HttpResponse('Measurement ' + measurement + ' updated')