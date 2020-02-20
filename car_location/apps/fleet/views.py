from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car
from .serializers import CarDetailSerializer, CarSerializer


class CarsListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    ordering_fields = ('id',)


class CarDetailsView(APIView):

    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        serializer = CarDetailSerializer(car)
        return Response(serializer.data)
