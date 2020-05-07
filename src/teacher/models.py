from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=25, null=False)
    email = models.CharField(max_length=40, null=True)
    gender = models.CharField(max_length=10, default='male', null=True)
    age = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
