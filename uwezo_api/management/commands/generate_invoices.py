from django.core.management.base import BaseCommand
from uwezo_api.tasks import generate_invoice  # Import the task function

class Command(BaseCommand):
    help = 'Generate invoices manually'

    def handle(self, *args, **options):
        # Call the task function directly
        generate_invoice()
        self.stdout.write(self.style.SUCCESS('Successfully generated invoices'))
