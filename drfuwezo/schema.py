# Import necessary modules
import graphene
from graphene import ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.fields import DjangoConnectionField
from uwezo_api.models import Partner  

# DjangoObjectType for the Partner model
class PartnerType(DjangoObjectType):
    class Meta:
        model = Partner

#Query class to expose queries for partners
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

class DocumentTypeEnum(graphene.Enum):
    NATIONAL_ID = 'National ID'
    PASSPORT = 'Passport'
    MILITARY_ID = 'Military ID'



class PartnerType(DjangoObjectType):
    class Meta:
        model = Partner

class CreatePartnerMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        middle_name = graphene.String()
        last_name = graphene.String()
        date_of_birth = graphene.Date()  
        # document_type = graphene.String()
        document_type = DocumentTypeEnum() 
        document_number = graphene.String()
        msisdn = graphene.String()
        email = graphene.String()
        document = graphene.String()

    partner = graphene.Field(PartnerType)

    @classmethod
    def mutate(cls, root, info):
        partner = Partner()  
        partner.save()
        return CreatePartnerMutation(partner=partner)

class Mutation(graphene.ObjectType):
    create_partner = CreatePartnerMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)






