from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_by_pk(id):
    measurement = Measurement.objects.get(pk=id)
    return measurement