from celery import shared_task
from .models import Account, Invoice, Driver
from django.utils import timezone
from django.db.models import Q
import logging
import datetime
from django.db import transaction

logger = logging.getLogger(__name__)


@shared_task
def generate_invoice():
    try:
        with transaction.atomic():
            # Calculation of the day of the week 
            day_of_week = datetime.datetime.today().weekday()
        
            # If it's Sunday, set day_of_run to 0
            if day_of_week == 6:
                day_of_run = '0'
            else:
                day_of_run = str(day_of_week + 1)

            # Query for accounts that match the conditions (status, day of week, mileage-based)
            accounts = Account.objects.filter(Q(status='active') | Q(status='delayed'),
                                              Q(mileage_based=False), Q(weekly_run=day_of_run))  

            for account in accounts:
                # Invoice with account details
                invoice = Invoice.objects.create(
                    account=account,
                    amount=account.weekly_amount,
                    balance=account.weekly_amount,
                    mileage=0,
                    issue_date=timezone.now(),
                    status='unpaid'  
                )

                # Log created invoice
                logger.info(f'Created invoice for account {account.id}')

                # Retrieve the associated driver for the account
                try:
                    driver = Driver.objects.get(contract__account=account)
                    driver_msisdn = driver.msisdn
                    logger.info(f'Driver MSISDN: {driver_msisdn}')
                except Driver.DoesNotExist:
                    driver_msisdn = "N/A"  # Default value when driver is not found
                    logger.warning("Driver not found for account %s", account.id)
                except Exception as e:
                    driver_msisdn = "Error"  # Default value for exceptions
                    logger.error("Error while retrieving driver: %s", e)

                # Save the invoice
                invoice.save()

            # Log message
            logger.info('generate_invoice Completed')
            
    except Exception as e:
        logger.error('generate_invoice FAILED: %s', e)
        
        # Return a failure message
        return "Invoice generation failed"
    
    # Return a success message
    return "Invoice generation successful"


