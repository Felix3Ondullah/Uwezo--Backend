# Import necessary modules
import graphene
from graphene import ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.fields import DjangoConnectionField
from uwezo_api.models import Partner  # Import your Partner model

# Define a DjangoObjectType for the Partner model
class PartnerType(DjangoObjectType):
    class Meta:
        model = Partner

# Define a Query class to expose queries for partners
# Define a Query class to expose queries for partners
class Query(ObjectType):
    # Query to retrieve a single partner by ID
    partner = graphene.Field(PartnerType, id=graphene.Int())

    # Query to retrieve all partners
    all_partners = graphene.List(PartnerType)

    def resolve_partner(self, info, id):
        return Partner.objects.get(pk=id)

    def resolve_all_partners(self, info,):
        return Partner.objects.all()


# Create a schema using the Query class
schema = graphene.Schema(query=Query)
