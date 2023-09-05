from rest_framework import serializers
from .models import  Transaction, Invoice, Partner, Vehicle, Driver, Tracker, Contract, Insurer, MobilePayment, Account



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

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class MobilePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePayment
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
