from django.db import models
from django.contrib.auth.models import User




# Global Variables for DOCUMENT_TYPE options
NATIONAL_ID = 'national_id'
PASSPORT = 'passport'
MILITARY_ID = 'military_id'
DOCUMENT_TYPE = [
	(NATIONAL_ID, ('National ID')),
	(PASSPORT, ('Passport')),
	(MILITARY_ID, ('Miliary ID')),
]

# Create your models here.
class Partner(models.Model):
	first_name = models.CharField(max_length=16)
	middle_name = models.CharField(max_length=16, null=True, blank=True)
	last_name = models.CharField(max_length=16)
	date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	document_type = models.CharField(max_length=16, choices=DOCUMENT_TYPE, default=NATIONAL_ID, null=True, blank=True)
	document_number = models.CharField(max_length=8, null=True, blank=True)
	msisdn = models.PositiveIntegerField()
	email = models.EmailField(max_length=255)
	document = models.TextField(null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		template = '{0.first_name} {0.last_name}'
		return template.format(self)
