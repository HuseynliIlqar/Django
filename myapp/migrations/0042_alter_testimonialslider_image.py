# Generated by Django 5.2 on 2025-04-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0041_alter_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialslider',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
