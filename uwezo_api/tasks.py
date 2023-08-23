from celery import shared_task
# from datetime import datetime
from pytz import timezone 
from .models import Account, Invoice
from django.utils import timezone
from django.db.models import Q
import logging
logger = logging.getLogger(__name__)



@shared_task
def generate_invoice():
    try:
        # Query for accounts that match the conditions (status, day of week, mileage-based)
        accounts = Account.objects.filter(Q(status='active') | Q(status='delayed'),
                                          Q(mileage_based=False), Q(weekly_run='1'))  
        
        for account in accounts:
            # invoice with account details
            invoice = Invoice.objects.create(
                account=account,
                amount=account.weekly_amount,
                balance=account.weekly_amount,
                mileage=0,
                issue_date=timezone.now(),
                status='unpaid'  
            )
            invoice.save()


        # Log messagees
        logger.info('generate_invoice Completed')
    except:
        logger.error('generate_invoice FAILED')
