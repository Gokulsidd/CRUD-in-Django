from random import *
from faker import Faker
from CrudApp.models import *
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CrudDemo.settings')

django.setup()
faker = Faker()


def generate(n):
    for i in range(n):
        femp_id = randint(101, 999)
        femp_name = faker.name()
        femp_age = randint(20, 50)
        femp_pnumber = ranint(900000, 999999)
        emp_record = Employee.objects.get_or_create(
            emp_id=femp_id, emp_name=femp_name, emp_age=femp_age, emp_pnumber=femp_pnumber)


generate(20)
