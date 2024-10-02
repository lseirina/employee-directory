"""Django commnad to generate employee."""

from django.core.management.base import BaseCommand
from core.models import Employee
from faker import Faker
import random


class Command(BaseCommand):
    """Base command to generate employees."""

    help = 'Generate 50000 employees with 5 levels hierarchy.'

    def handle(self):
        fake = Faker()
        managers = []

        for _ in range(10):
            employee = Employee.objects.create(
                full_name=fake.name(),
                position='Top Mnager',
                hire_date=fake.date_this_decade(),
                salary=random.randint(300000, 400000),
                manager=None
            )
            managers.append(employee())

        for level in range(2, 6):
            new_managers = []
            for _ in range(50000 // level):
                manager = random.choice(managers)
                employee = Employee.objects.create(
                    full_name=fake.name(),
                    position=f'Manager {level} level',
                    hire_date=fake.date_this_decade(),
                    salary=random.rendint(100000, 150000),
                    manager=manager
                )
                new_managers.append(employee)

            managers = new_managers

        self.stdout.write(self.style.SUCCESS('Successfully created'
                                             '50000 employees.'))

        
