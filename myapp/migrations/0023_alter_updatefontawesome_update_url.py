# Generated by Django 5.2 on 2025-04-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_updatefontawesome_read_me_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatefontawesome',
            name='update_url',
            field=models.TextField(default='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css', max_length=300),
        ),
    ]
