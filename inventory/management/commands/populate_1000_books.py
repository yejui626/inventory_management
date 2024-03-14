

from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from random import randint
from inventory.models import Book, Supplier

class Command(BaseCommand):
    help = 'Populate the database with 1000 books'

    def handle(self, *args, **kwargs):
        suppliers = Supplier.objects.filter(
                name='Oxford University Press'
            )

        for i in range(1000):
            if suppliers.exists():
                supplier = suppliers.first()
            else:
                # Create a new supplier if none exists
                supplier = Supplier.objects.create(
                    name=f'Oxford University Press {i+1}',
                    contact_person='Goo Ye Jui',
                    email='yjyejui626@gmail.com',
                    phone_number='0184040438',
                    address = 'Oxford University Press, Educational Supply Section, North Kettering Business Park, Hipwell Road, Kettering, Northamptonshire. NN14 1UA',
                    currency = 'GBP'
                )
            book = Book.objects.create(
                title=f"Book {i+1}",
                author=f"Author {i+1}",
                category=f"Category {i+1}",
                price=randint(10, 200),  
                quantity=randint(1, 50),  
                publication_date=datetime.now().date() - timedelta(days=randint(1, 365*10)),  
                isbn=str(randint(1000000000000, 9999999999999)),
                image_url=f"/images/{i+1}.png",
                supplier=supplier
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 1000 books'))
