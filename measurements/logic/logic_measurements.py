from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_by_pk(measurement_id):
    measurement = Measurement.objects.get(pk=measurement_id)
    return measurement