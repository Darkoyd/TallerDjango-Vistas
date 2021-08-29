from django.urls import path
from . import views

urlpatterns = [

    path('list/', views.get_measurements, name='measurementsList'),
    path('<int:measurement_id>/', views.get_measurement, name='measurementByPk'),
    path('delete/<int:measurement_id>', views.delete_measurement, name='measurementDeleteByPk'),
    path('update/<int:measurement_id>/<float:new_value>', views.update_measurement, name='measurementUpdateByPk'),
]