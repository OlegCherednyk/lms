import datetime
import random

from django.db import models

# Create your models here.
from faker import Faker

from group.models import Group


class Student(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=40, null=True)
    birthdate = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(max_length=25, null=False)
    group = models.ForeignKey(to=Group, null=True, on_delete=models.SET_NULL, related_name='student')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.phone_number} {self.group}'

    @classmethod
    def gen_student(cls, groups=None):
        faker = Faker()
        if groups is None:
            group = list(Group.objects.all())
        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            phone_number=faker.phone_number(),
            group=random.choice(group)
        )
        student.save()
