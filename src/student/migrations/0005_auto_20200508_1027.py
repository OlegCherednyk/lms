# Generated by Django 2.2.12 on 2020-05-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(default=0, max_length=14),
        ),
    ]
