# Generated by Django 3.1.4 on 2021-01-18 17:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
