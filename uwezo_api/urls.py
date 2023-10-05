# from django.urls import path, include
# from .views import TransactionViewSets, InvoiceViewSets, AccountViewSets, MobilePaymentViewSets, ContractViewSets, PartnerViewSets, VehicleViewSets, InsurerViewSets, DriverViewSets, TrackerViewSets
# from rest_framework import routers

# router = routers.SimpleRouter()

# router.register('partner',PartnerViewSets, basename= 'partner')
# router.register('vehicle',VehicleViewSets, basename= 'vehicle')
# router.register('insurer',InsurerViewSets, basename= 'insurer')
# router.register('driver',DriverViewSets, basename= 'driver')
# router.register('tracker',TrackerViewSets, basename= 'tracker')
# router.register('contract',ContractViewSets, basename= 'contract')
# router.register('mobilepayment',MobilePaymentViewSets, basename= 'mobilepayment')
# router.register('account',AccountViewSets, basename= 'account')
# router.register('invoice',InvoiceViewSets, basename= 'invoice')
# router.register('transaction',TransactionViewSets, basename= 'transaction')




# urlpatterns = [
# path('', include (router.urls)),
# ]

from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView #View for the user interface
from drfuwezo.schema import schema #Schema we want to query

urlpatterns = [
    path('admin/', admin.site.urls),
    # This URL will provide a user interface that is used to query the database
    # and interact with the GraphQL API.
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]