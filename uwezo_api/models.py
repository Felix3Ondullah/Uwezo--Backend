from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# To enable calling task by name to avoid circular import dependency import celery
# import celery
import uuid

# Global Variables for STATUS options
ON = 'on'
OFF = 'off'
INACTIVE = 'inactive'

STATUS = [
	(ON, ('On')),
	(OFF, ('Off')),
	(INACTIVE, ('Inactive')),
]

# Global Variables for VALID_STATUS options
VALID = 'Valid'
INVALID = 'Invalid'
VALID_STATUS = [
	(VALID, ('Valid')),
	(INVALID, ('Invalid')),
]


# Global Variables for DOCUMENT_TYPE options
NATIONAL_ID = 'national_id'
PASSPORT = 'passport'
MILITARY_ID = 'military_id'
DOCUMENT_TYPE = [
	(NATIONAL_ID, ('National ID')),
	(PASSPORT, ('Passport')),
	(MILITARY_ID, ('Military ID')),
]


ACTIVE = 'active'
SUSPENDED = 'suspended'
CLOSED = 'closed'

IDENTITY_STATUS = [
	(ACTIVE, ('Active')),
	(SUSPENDED, ('Suspended')),
	(CLOSED, ('Closed')),
]

BANK = 'bank'
CASH = 'cash'
MPESA = 'mpesa'

# Create your models here.
class Partner(models.Model):
	first_name = models.CharField(max_length=16)
	middle_name = models.CharField(max_length=16, null=True, blank=True)
	last_name = models.CharField(max_length=16)
	date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	document_type = models.CharField(max_length=16, choices=DOCUMENT_TYPE, default=NATIONAL_ID, null=True, blank=True)
	document_number = models.CharField(max_length=8, null=True, blank=True)
	msisdn = models.PositiveBigIntegerField( help_text="Kenyan mobile number in the format +254XXXXXXXXX")
	email = models.EmailField(max_length=255)
	document = models.TextField(null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		template = '{0.first_name} {0.last_name}'
		return template.format(self)

class Vehicle(models.Model):
	partner = models.ForeignKey('Partner', on_delete=models.CASCADE)
	registration = models.CharField(max_length=7, unique = True)
	make = models.CharField(max_length=16)
	model = models.CharField(max_length=16)
	yom = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2099)])
	logbook = models.TextField(blank=True, null=True)
	chasis_no = models.CharField(max_length=32, blank=True, null=True)
	engine_no = models.CharField(max_length=32, blank=True, null=True)
	#ntsa_status = models.CharField(max_length=16, choices=VALID_STATUS, default=INVALID)
	#uber_status = models.CharField(max_length=16, choices=VALID_STATUS, default=INVALID)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.registration


class Driver(models.Model):
	first_name = models.CharField(max_length=16)
	middle_name = models.CharField(max_length=16, blank=True)
	last_name = models.CharField(max_length=16)
	date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
	document_type = models.CharField(max_length=16, choices=DOCUMENT_TYPE, default=NATIONAL_ID)
	document_number = models.CharField(max_length=8)
	msisdn = models.PositiveBigIntegerField( help_text="Kenyan mobile number in the format +254XXXXXXXXX")
	email = models.EmailField(max_length=255)
	document = models.TextField(blank=True)
	status = models.CharField(max_length=16, choices=IDENTITY_STATUS, default=ACTIVE)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	partner = models.ForeignKey('Partner', on_delete=models.CASCADE, null=True)
	#id_document = models.FileField(upload_to='id_documents/', max_length=100, null=True, blank=True, help_text="Upload an ID document (PDF or image, max 5MB)")

	def __str__(self):
		template = '{0.first_name} {0.last_name}'
		return template.format(self)

class Insurer(models.Model):
	name = models.CharField(max_length=32, unique=True)
	claim_form = models.TextField(blank=True)
	windscreen_form = models.TextField(blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


# Models for Vehicle Compliance
class Tracker(models.Model):
	PROTRACK = 'protrack'
	WHATSGPS = 'whatsgps'

	TRACKER = [
		(PROTRACK, ('ProTrackGPS')),
		(WHATSGPS, ('WhatsGPS')),
	]
	vehicle = models.OneToOneField('Vehicle', on_delete=models.CASCADE)
	accesstoken = models.ForeignKey('AccessToken', on_delete=models.SET_NULL, blank=True, null=True)
	msisdn = models.PositiveIntegerField()
	imei = models.BigIntegerField(default=0)
	car_id = models.PositiveIntegerField(default=0)
	platform = models.CharField(max_length=16, choices=TRACKER, default=PROTRACK)
	autoswitch = models.BooleanField(default=True)
	expiry_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	status = models.CharField(max_length=16, choices=STATUS, default=INACTIVE)
	command = models.CharField(max_length=8, blank=True)
	command_response = models.BooleanField(default=False)
	document = models.TextField(blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	

class Insurance(models.Model):
	insurer = models.ForeignKey('Insurer', on_delete=models.CASCADE)
	vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
	policy_number = models.CharField(max_length=255)
	issue_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	expiry_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	status = models.CharField(max_length=16, choices=VALID_STATUS, default=VALID)
	document = models.TextField(blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	

class NtsaInspection(models.Model):
	vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
	vc_number = models.CharField(max_length=7, unique=True)
	booking_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	expiry_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	document = models.TextField(blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.vc_number


class UberInspection(models.Model):
	vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
	booking_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	expiry_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	document = models.TextField(blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	


# Models for Driver Compliance
class DriverLicense(models.Model):
	driver = models.OneToOneField('Driver', on_delete=models.CASCADE, unique=True)
	license_number = models.CharField(max_length=8, unique=True)
	license_status = models.CharField(max_length=32, choices=VALID_STATUS, default=VALID)
	psv_status = models.CharField(max_length=16, choices=VALID_STATUS, default=VALID)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.license_number


class LicenseRenewal(models.Model):
	driverlicense = models.ForeignKey('DriverLicense', on_delete=models.CASCADE)
	expiry_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	document = models.TextField(blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		template = '{0.driverlicense}'
		return template.format(self)


class PsvRenewal(models.Model):
	driverlicense = models.ForeignKey('DriverLicense', on_delete=models.CASCADE)
	expiry_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	document = models.TextField(blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		template = '{0.driverlicense}'
		return template.format(self)
	

# Models for The contract
class Contract(models.Model):
	ACTIVE = 'active'
	PERFORMING = 'performing'
	SUBSTANDARD = 'substandard'
	WATCH = 'watch'
	TERMINATED = 'terminated'
	INACTIVE = 'inactive'
	CLOSED = 'closed'

	CONTRACT_STATUS = [
		(ACTIVE, ('Active')),
		(PERFORMING, ('Performing')),
		(SUBSTANDARD, ('Substandard')),
		(ACTIVE, ('Active')),
		(OFF, ('Off')),
		(INACTIVE, ('Inactive')),
		]
	vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
	driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
	start_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	end_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	document = models.TextField(blank=True, null=True)
	status = models.CharField(max_length=16, choices=CONTRACT_STATUS, default=ACTIVE)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)   

	def __str__(self):
		template = '{0.vehicle}-{0.driver}'
		return template.format(self)
	

#Models for Finance & Accounts
class Account(models.Model):
	ACTIVE = 'active'
	DELAYED = 'delayed'
	DEFAULTED = 'defaulted'
	HOLD = 'hold'

	ACCOUNT_STATUS = [
	(ACTIVE, ('Active')),
	(DELAYED, ('Delayed')),
	(DEFAULTED, ('Defaulted')),
	(HOLD, ('Hold')),   
	]

	SUNDAY = '0'
	MONDAY = '1'
	TUESDAY = '2'
	WEDNESDAY = '3'
	THURSDAY = '4'
	FRIDAY = '5'
	SATURDAY = '6'

	RUN_DAY = [
	(SUNDAY, ('Sunday')),
	(MONDAY, ('Monday')),
	(TUESDAY, ('Tuesday')),
	(WEDNESDAY, ('Wednesday')),
	(THURSDAY, ('Thursday')),
	(FRIDAY, ('Friday')),
	(SATURDAY, ('Saturday')),
	]

	contract = models.OneToOneField('Contract', on_delete=models.CASCADE)
	weekly_amount = models.PositiveSmallIntegerField(default=0)
	weekly_run = models.CharField(max_length=16, choices=RUN_DAY, default=THURSDAY)
	mileage_based = models.BooleanField(default=True)
	price_per_km = models.PositiveSmallIntegerField(default=0)
	weeks = models.PositiveSmallIntegerField(default=0)
	paid_amount = models.PositiveIntegerField(default=0)
	status = models.CharField(max_length=16, choices=ACCOUNT_STATUS, default=ACTIVE)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		template = '{0.contract}'
		return template.format(self)   
	

class Invoice(models.Model):
	PAID = 'paid'
	UNPAID = 'unpaid'
	PARTIAL = 'partial'
	DEFAULT = 'default'

	INVOICE_STATUS = [
		(PAID, ('Paid')),
		(UNPAID, ('Unpaid')),
		(PARTIAL, ('Partial')),
		(DEFAULT, ('Default'))
	]

	account = models.ForeignKey('Account', on_delete=models.CASCADE)
	amount = models.PositiveIntegerField()
	paid_amount = models.PositiveIntegerField(default=0)
	balance = models.PositiveIntegerField(default=0)
	mileage = models.PositiveIntegerField(default=0)
	issue_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	status = models.CharField(max_length=16, choices=INVOICE_STATUS, default=UNPAID)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		template = '{0.account}'
		return template.format(self)
	
class MobilePayment(models.Model):
	# Options in the event of using STK Push Payments
	INITIATED = 'initiated'
	PENDING = 'pending'
	COMPLETED = 'completed'
	CANCELLED = 'cancelled'

	RECEIPT_STATUS = [
		(INITIATED, ('Initiated')),
		(PENDING, ('Pending')),
		(COMPLETED, ('Completed')),
		(CANCELLED, ('Cancelled')),
	]

	invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
	receipt = models.CharField(max_length=16)
	transaction_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	status = models.CharField(max_length=16, choices=RECEIPT_STATUS, default= PENDING)
	split = models.BooleanField(default=False)
	index = models.PositiveSmallIntegerField()
	amount = models.PositiveIntegerField()
	split_amount = models.PositiveIntegerField()
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.receipt
	
# Models for Maintenance and Parts
class MaintenanceProvider(models.Model):
	name = models.CharField(max_length=32, unique=True)
	address = models.CharField(max_length=255)
	msisdn = models.PositiveIntegerField()
	status = models.CharField(max_length=16, choices=IDENTITY_STATUS, default=ACTIVE)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class VehicleMaintenance(models.Model):
	ROUTINE = 'routine'
	ADHOC = 'adhoc'
	POST_ACCIDENT = 'post_accident'

	MAINTENANCE_TYPE = [
		(ROUTINE, ('Routine')),
		(ADHOC, ('Adhoc')),
		(POST_ACCIDENT, ('Post Accident')),
	]

	contract = models.ForeignKey('Contract', on_delete=models.CASCADE)
	provider = models.ForeignKey('MaintenanceProvider', on_delete=models.CASCADE)
	mileage = models.PositiveIntegerField()
	amount = models.PositiveIntegerField()
	maintenace_type = models.CharField(max_length=16, choices=MAINTENANCE_TYPE, default=ROUTINE)
	maintenance_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		template = '{0.contract}'
		return template.format(self)
	

class SparePart(models.Model):
	name = models.CharField(max_length=32, unique=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class MaintenancePart(models.Model):
	vehiclemaintenance = models.ForeignKey('VehicleMaintenance', on_delete=models.CASCADE)
	sparepart = models.ForeignKey('SparePart', on_delete=models.CASCADE)
	quantity = models.PositiveSmallIntegerField()
	unit_price = models.PositiveSmallIntegerField()
	amount = models.PositiveSmallIntegerField()
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		template = '{0.vehiclemaintenance}'
		return template.format(self)
	
class AccessToken(models.Model):
	PROTRACK = 'protrack'
	WHATSGPS = 'whatsgps'

	TRACKER = [
		(PROTRACK, ('ProTrackGPS')),
		(WHATSGPS, ('WhatsGPS')),
	]
	username = models.CharField(max_length=64, unique=True)
	password = models.CharField(max_length=64)
	platform = models.CharField(max_length=16, choices=TRACKER, default=PROTRACK)
	access_token = models.CharField(max_length=64, default='Test')

	def __str__(self):
		return self.username


class MpesaAccessToken(models.Model):
	access_token = models.CharField(max_length=64)


class Transaction(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	TransactionType = models.CharField(max_length=64)
	TransID = models.CharField(max_length=50, blank=False, unique=True)
	TransAmount = models.IntegerField()
	MSISDN = models.BigIntegerField()
	FirstName = models.CharField(max_length=200, null=False)
	MiddleName = models.CharField(max_length=200, blank=True, null=True)
	LastName = models.CharField(max_length=200, null=True, blank=True)
	BillRefNumber = models.CharField(max_length=200, blank=True, null=True)
	TransTime = models.CharField(max_length=200, blank=True, null=True)
	Reconciled = models.BooleanField(default=False)
	ReconciledCounter = models.IntegerField(default=0)
	Unallocated = models.IntegerField(default=0)
	Invoice = models.ForeignKey(Invoice, null=True, blank=True, on_delete=models.CASCADE)
	CreateDate = models.DateTimeField(auto_now_add=True)
	UpdateDate = models.DateTimeField(auto_now=True)


class Mileage(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	account = models.ForeignKey(Account, related_name="mileages", on_delete=models.CASCADE)
	mileage = models.DecimalField(max_digits=10, decimal_places=2)
	mileage_date = models.CharField(max_length=200, null=True, blank=False)
	invoiced_status = models.BooleanField(default=False)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

class VehicleMake(models.Model):
	name = models.CharField(max_length=32)
	
	def __str__(self):
		return self.name


class VehicleModel(models.Model):
	name = models.CharField(max_length=32)
	make = models.ForeignKey(VehicleMake, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
