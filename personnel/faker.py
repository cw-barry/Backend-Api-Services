'''
    # https://faker.readthedocs.io/en/master/
    $ pip install faker # install faker module
    python manage.py flush # delete all exists data from db. dont forget: createsuperuser
    python manage.py shell
    from personnel_app.faker import run
    run()
    exit()
'''

from .models import Personnel, Department
from django.contrib.auth.models import User
import random
from faker import Faker
from django.contrib.auth.models import User
from django.utils.timezone import datetime, now
from pytz import timezone as tz

def add_department():
    departments = ["Full Stack", "Data Science", "HR", "Sales", "Marketing", "AWS Devops", "Cyber"]
    for i in departments:
        Department.objects.create(name=i)
    
    print("Departments added")

def add_personnel():


    qs_department = Department.objects.all()
    fake = Faker()

    GENDER =(
            ("Female", "2"),
            ("Male", "1"),
            ("Prefer Not Say", "3"),
        )
    for i in range(100):
        data = {}
        data["first_name"] = fake.first_name()
        data["last_name"] = fake.last_name()
        department = random.randint(0,len(qs_department)-1)
        data["department"] = qs_department[department]

        data["title"] = fake.job()
        gender = random.sample(GENDER,1)
        data["gender"] = gender[0][1]
        data["email"] = f'{data["last_name"]}.{data["first_name"]}@clarusway.com'
        data["date_joined"] = tz("UTC").localize(fake.date_time_between(
            start_date=datetime(2023, 3, 1),
            end_date=now()
        ))
        data["image"] = fake.image_url()


        Personnel.objects.create(**data)
    
    print("Fake personnel added")

def run():
    print('Fake data generation started')
    Personnel.objects.all().delete()
    Department.objects.all().delete()
    add_department()
    add_personnel()
    print('Fake data generation completed')