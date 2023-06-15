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
import requests


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
            ("Person", "3"),
        )
    for i in range(200):
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

        # res = requests.get('https://source.unsplash.com/random/900x700/?'+gender[0][0])
        # print(res.url)

        # if gender[0][1] == '1':
        #     # user_image_url = fake.random_element(elements=fake.providers.person.Provider.male_avatar)
        #     user_image_url = fake.avatar_url(gender="male")
        # elif gender[0][1] == '2':
        #     user_image_url = fake.avatar_url(gender="female")
        # else:
        #     user_image_url = fake.image_url()
        
        data["image"] = fake.image_url()
        # fake.generator.random_element(random.choice([fake.providers.person.Provider.male_avatar, fake.providers.person.Provider.female_avatar]))
        # fake.image_url(width=None, height=None, category=None, randomize=True, gender=gender[0][0])
        Personnel.objects.create(**data)
    
    print("Fake personnel added")

def run():
    print('Fake data generation started')
    Personnel.objects.all().delete()
    Department.objects.all().delete()
    add_department()
    add_personnel()
    print('Fake data generation completed')