from django.db import models

# Create your models here.
from faker import Faker

from teacher.models import Teacher


class Group(models.Model):
    group_num = models.IntegerField(null=False, default=0)
    teachers = models.ForeignKey(to=Teacher, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.group_num}'
