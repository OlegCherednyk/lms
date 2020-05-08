import datetime

from django.db import models

# Create your models here.
from faker import Faker


class Student(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=40, null=True)
    birthdate = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(max_length=14, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.phone_number}'

    @classmethod
    def gen_student(cls):
        faker = Faker()

        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            phone_number=faker.phone_number()
        )
        student.save()
