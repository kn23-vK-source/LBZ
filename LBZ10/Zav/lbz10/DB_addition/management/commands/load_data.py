from django.core.management.base import BaseCommand
from DB_addition.models import Supplier, Material, Delivery
from faker import Faker
import random

fake = Faker('uk_UA')

class Command(BaseCommand):
    help = 'Load fake data into the database'

    def handle(self, *args, **kwargs):
        # Insert materials
        materials_data = [
            ("Деревина", round(random.uniform(10.00, 50.00), 2)),
            ("Лак", round(random.uniform(5.00, 20.00), 2)),
            ("Сталеві деталі", round(random.uniform(20.00, 100.00), 2))
        ]
        for material in materials_data:
            Material.objects.create(material_name=material[0], price=material[1])

        # Insert suppliers
        suppliers_data = [
            (fake.company(), fake.name(), fake.phone_number(), str(fake.random_int(min=100000, max=999999))),
            (fake.company(), fake.name(), fake.phone_number(), str(fake.random_int(min=100000, max=999999))),
            (fake.company(), fake.name(), fake.phone_number(), str(fake.random_int(min=100000, max=999999))),
            (fake.company(), fake.name(), fake.phone_number(), str(fake.random_int(min=100000, max=999999)))
        ]
        for supplier in suppliers_data:
            Supplier.objects.create(company_name=supplier[0], contact_person=supplier[1], phone=supplier[2], account_number=supplier[3])

        # Insert deliveries
        for _ in range(22):
            supplier_id = random.randint(1, 4)
            material_id = random.randint(1, 3)
            delivery_date = fake.date_between(start_date='-1y', end_date='today')
            delivery_days = random.randint(1, 7)
            quantity = random.randint(1, 100)
            Delivery.objects.create(
                delivery_date=delivery_date,
                supplier_id=supplier_id,
                material_id=material_id,
                delivery_days=delivery_days,
                quantity=quantity
            )

        self.stdout.write(self.style.SUCCESS('Fake data loaded successfully'))

        

