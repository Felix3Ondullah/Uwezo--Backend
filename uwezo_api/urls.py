from django.urls import path, include
from .views import TransactionViewSets, InvoiceViewSets, AccountViewSets, MobilePaymentViewSets, ContractViewSets, PartnerViewSets, VehicleViewSets, InsurerViewSets, DriverViewSets, TrackerViewSets
from rest_framework import routers

router = routers.SimpleRouter()

router.register('partner',PartnerViewSets, basename= 'partner')
router.register('vehicle',VehicleViewSets, basename= 'vehicle')
router.register('insurer',InsurerViewSets, basename= 'insurer')
router.register('driver',DriverViewSets, basename= 'driver')
router.register('tracker',TrackerViewSets, basename= 'tracker')
router.register('contract',ContractViewSets, basename= 'contract')
router.register('mobilepayment',MobilePaymentViewSets, basename= 'mobilepayment')
router.register('account',AccountViewSets, basename= 'account')
router.register('invoice',InvoiceViewSets, basename= 'invoice')
router.register('transaction',TransactionViewSets, basename= 'transaction')




urlpatterns = [
path('', include (router.urls)),
]