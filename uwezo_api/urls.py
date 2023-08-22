from django.urls import path, include
from .views import PartnerViewSets, VehicleViewSets, InsurerViewSets, DriverViewSets, TrackerViewSets
from rest_framework import routers

router = routers.SimpleRouter()

router.register('partner',PartnerViewSets, basename= 'partner')
router.register('vehicle',VehicleViewSets, basename= 'vehicle')
router.register('insurer',InsurerViewSets, basename= 'insurer')
router.register('driver',DriverViewSets, basename= 'driver')
router.register('tracker',TrackerViewSets, basename= 'tracker')


urlpatterns = [
path('', include (router.urls)),
]