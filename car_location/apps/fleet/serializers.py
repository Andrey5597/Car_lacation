from faker import Faker
from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarDetailSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()

    def get_location(self, obj):
        fake = Faker()
        return {
            'latitude': fake.latitude(),
            'longitude': fake.longitude()
        }

    class Meta:
        model = Car
        fields = ('location',)
