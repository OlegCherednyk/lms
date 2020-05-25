# Generated by Django 2.2.12 on 2020-05-23 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_group_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='teachers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group', to='teacher.Teacher'),
        ),
    ]
