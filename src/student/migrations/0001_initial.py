# Generated by Django 2.2.12 on 2020-05-01 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=40, null=True)),
                ('birthdate', models.DateField(default=datetime.date(2020, 5, 1))),
            ],
        ),
    ]
