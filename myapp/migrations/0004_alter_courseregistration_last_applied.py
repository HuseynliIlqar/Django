# Generated by Django 5.2 on 2025-04-07 10:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_courseregistration_last_applied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseregistration',
            name='last_applied',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
