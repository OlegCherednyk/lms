from django.db import models

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=40, null=True)
    phone_number = models.CharField(max_length=14, null=False)
    gender = models.CharField(max_length=10, default='male', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.phone_number}"
