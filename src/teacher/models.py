from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=25, null=False)
    email = models.CharField(max_length=40,null=True)
    gender = models.CharField(max_length=10,default='male',null=False)
    age = models.IntegerField(null=False)