from django.shortcuts import render
from .models import  Transaction, Invoice, Partner, Vehicle, Insurer, Driver , Tracker, Contract, MobilePayment, Account
from .serializers import TransactionSerializer, InvoiceSerializer, AccountSerializer, MobilePaymentSerializer, ContractSerializer, TrackerSerializer, PartnerSerializer, VehicleSerializer,InsurerSerializer, DriverSeializer
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

class TrackerViewSets(viewsets.GenericViewSet, mixins.UpdateModelMixin,mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer

class ContractViewSets(viewsets.GenericViewSet, mixins.UpdateModelMixin,mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class MobilePaymentViewSets(viewsets.GenericViewSet, mixins.UpdateModelMixin,mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset= MobilePayment.objects.all()
    serializer_class = MobilePaymentSerializer

class AccountViewSets(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.CreateModelMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class InvoiceViewSets(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
 
class TransactionViewSets(viewsets. GenericViewSet, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
