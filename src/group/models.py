from django.db import models

# Create your models here.
from faker import Faker


class Group(models.Model):
    group_num = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f'{self.group_num}'
