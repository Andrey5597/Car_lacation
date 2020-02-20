from django.urls import path

from .views import CarDetailsView, CarsListView

urlpatterns = [
    path('cars/', CarsListView.as_view(), name='all cars'),
    path('cars/<car_id>/', CarDetailsView.as_view(), name='car details')
]
