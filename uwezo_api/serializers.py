from rest_framework import serializers
from .models import Partner, Vehicle, Driver, Tracker

from rest_framework import serializers
from .models import Partner, Vehicle, Driver, Insurer

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Vehicle
        fields = '__all__'

class DriverSeializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class InsurerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurer
        fields = '__all__'

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = '__all__'