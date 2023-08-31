from celery import shared_task
from .models import Account, Invoice, Driver, Transaction, MobilePayment
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
            print(accounts)

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



# Shared task to process a full payment
@shared_task
def process_full_payment(payment_id):
    try:
        payment = MobilePayment.objects.get(id=payment_id)

        if payment.status != MobilePayment.PENDING:
            logger.warning(f"Payment {payment_id} is not in pending status.")
            return "Payment Unsuccessful - Payment is not in pending status."

        # Fetch related invoice and driver
        invoice = payment.invoice
        driver = Driver.objects.get(contract__account=invoice.account)

        # Extract driver details
        msisdn = driver.msisdn
        first_name = driver.first_name
        middle_name = driver.middle_name
        last_name = driver.last_name

        # Prepare transaction data
        transaction_data = {
            'TransactionType': 'Payment',
            'TransID': payment.receipt,
            'TransAmount': payment.amount,
            'MSISDN': msisdn,
            'FirstName': first_name,
            'MiddleName': middle_name,
            'LastName': last_name,
            'BillRefNumber': '',
            'TransTime': str(payment.transaction_date),
            'Reconciled': True,
            'ReconciledCounter': 1,
            'Unallocated': 0,
            'Invoice': invoice,
        }

        # Create a transaction
        transaction = Transaction.objects.create(**transaction_data)

        # Update invoice details
        invoice.paid_amount += payment.amount
        invoice.balance -= payment.amount

        # Update invoice status if balance is zero
        if invoice.balance == 0:
            invoice.status = Invoice.PAID

        # Update payment status and save changes
        payment.status = MobilePayment.COMPLETED
        invoice.save()
        payment.save()

        logger.info(f"Full Payment processed for Payment {payment_id}")
        return "Payment Successful"
    except MobilePayment.DoesNotExist:
        logger.error(f"Payment {payment_id} does not exist.")
        return "Payment Unsuccessful - Payment ID does not exist"
    except Driver.DoesNotExist:
        logger.error(f"Driver not found for payment {payment_id}.")
        return "Payment Unsuccessful - Driver not found"
    except Exception as e:
        logger.error(f"Error processing full payment: {str(e)}")
        return "Payment Unsuccessful - An error occurred"

# Shared task to process a partial payment
@shared_task
def process_partial_payment(payment_id, partial_amount):
    try:
        payment = MobilePayment.objects.get(id=payment_id)

        if payment.status != MobilePayment.PENDING:
            logger.warning(f"Payment {payment_id} is not in pending status.")
            return "Payment Unsuccessful - Payment is not in pending status."

        if partial_amount <= 0:
            logger.warning("Partial amount must be greater than zero.")
            return "Payment Unsuccessful - Partial amount must be greater than zero."

        # Fetch related invoice and driver
        invoice = payment.invoice
        driver = Driver.objects.get(contract__account=invoice.account)

        # Extract driver details
        msisdn = driver.msisdn
        first_name = driver.first_name
        middle_name = driver.middle_name
        last_name = driver.last_name

        # Prepare transaction data for partial payment
        transaction_data = {
            'TransactionType': 'Payment',
            'TransID': payment.receipt,
            'TransAmount': partial_amount,
            'MSISDN': msisdn,
            'FirstName': first_name,
            'MiddleName': middle_name,
            'LastName': last_name,
            'BillRefNumber': '',
            'TransTime': str(payment.transaction_date),
            'Reconciled': True,
            'ReconciledCounter': 1,
            'Unallocated': 0,
            'Invoice': invoice,
        }

        # Create a transaction
        transaction = Transaction.objects.create(**transaction_data)

        # Update invoice details
        invoice.paid_amount += partial_amount
        invoice.balance -= partial_amount

        # Update invoice status based on balance
        if invoice.balance == 0:
            invoice.status = Invoice.PAID
        else:
            invoice.status = Invoice.PARTIAL
            
            # Create a new invoice for the remaining balance
            new_invoice = Invoice.objects.create(
                account=invoice.account,
                amount=invoice.balance,
                balance=invoice.balance,
                mileage=0,
                issue_date=timezone.now(),
                status=Invoice.UNPAID
            )

        # Update payment status and save changes
        payment.status = MobilePayment.COMPLETED
        invoice.save()
        payment.save()

        logger.info(f"Partial Payment processed for Payment {payment_id}")
        return "Payment Successful"
    except MobilePayment.DoesNotExist:
        logger.error(f"Payment {payment_id} does not exist.")
        return "Payment Unsuccessful - Payment ID does not exist"
    except Driver.DoesNotExist:
        logger.error(f"Driver not found for payment {payment_id}.")
        return "Payment Unsuccessful - Driver not found"
    except Exception as e:
        logger.error(f"Error processing partial payment: {str(e)}")
        return "Payment Unsuccessful - An error occurred"
