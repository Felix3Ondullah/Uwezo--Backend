# from django.contrib import admin
# from .models import Mileage, VehicleModel, VehicleMake, AccessToken, MpesaAccessToken, Transaction, SparePart, MaintenancePart, VehicleMaintenance, MaintenanceProvider, Partner, MobilePayment, Invoice, Account, Contract, Vehicle, Driver, Insurer, Tracker, Insurance, NtsaInspection, UberInspection, DriverLicense, LicenseRenewal, PsvRenewal

# # Register your models here.
# admin.site.register(Partner)
# admin.site.register(Vehicle)
# admin.site.register(Driver)
# admin.site.register(Insurer)
# admin.site.register(Tracker)
# admin.site.register(Insurance)
# admin.site.register(NtsaInspection)
# admin.site.register(UberInspection)
# admin.site.register(DriverLicense)
# admin.site.register(LicenseRenewal)
# admin.site.register(Contract)
# admin.site.register(Account)
# admin.site.register(Invoice)
# admin.site.register(MobilePayment)
# admin.site.register(VehicleMaintenance)
# admin.site.register(MaintenanceProvider)
# admin.site.register(MaintenancePart)
# admin.site.register(SparePart)
# admin.site.register(AccessToken)
# admin.site.register(MpesaAccessToken)
# admin.site.register(Transaction)
# admin.site.register(Mileage)
# admin.site.register(VehicleMake)
# admin.site.register(VehicleModel)

from django.contrib import admin
from .models import Partner
admin.site.register(Partner)