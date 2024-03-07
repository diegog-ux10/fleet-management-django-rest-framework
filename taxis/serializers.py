from rest_framework import serializers
from .models import Taxi, Trayectory  # Import your models correctly

class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = ['id', 'plate']
        read_only_fields = ['id']  # id is read-only

class TrayectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trayectory
        fields = ['id', 'date', 'taxi_id', 'latitude', 'longitude']
        read_only_fields = ['id']  # These fields are read-only
