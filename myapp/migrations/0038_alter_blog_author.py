# Generated by Django 5.2 on 2025-04-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_alter_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.TextField(blank=True),
        ),
    ]
