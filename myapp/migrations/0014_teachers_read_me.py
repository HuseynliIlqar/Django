# Generated by Django 5.2 on 2025-04-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_teachers_read_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='READ_ME',
            field=models.CharField(default='test', editable=False),
        ),
    ]
