from django.shortcuts import render
from .models import Partner, Vehicle, Insurer, Driver
from .serializers import PartnerSerializer, VehicleSerializer,InsurerSerializer, DriverSeializer
from rest_framework import mixins
from rest_framework import viewsets


# Create your views here.
class PartnerViewSets(viewsets.GenericViewSet, mixins.CreateModelMixin,mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class VehicleViewSets(viewsets.GenericViewSet, mixins.UpdateModelMixin,mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class InsurerViewSets(viewsets.GenericViewSet, mixins.UpdateModelMixin,mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Insurer.objects.all()
    serializer_class = InsurerSerializer

class DriverViewSets(viewsets.GenericViewSet, mixins.UpdateModelMixin,mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Driver.objects.all()
    serializer_class = DriverSeializer
 