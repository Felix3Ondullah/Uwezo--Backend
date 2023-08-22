from django.urls import path, include
from .views import PartnerViewSets, VehicleViewSets, InsurerViewSets, DriverViewSets
from rest_framework import routers

router = routers.SimpleRouter()

router.register('partner',PartnerViewSets, basename= 'partner')
router.register('vehicle',VehicleViewSets, basename= 'vehicle')
router.register('insurer',InsurerViewSets, basename= 'insurer')
router.register('driver',DriverViewSets, basename= 'driver')



urlpatterns = [
path('', include (router.urls)),
]