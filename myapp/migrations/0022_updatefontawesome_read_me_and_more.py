# Generated by Django 5.2 on 2025-04-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_rename_update_font_awesome_updatefontawesome'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatefontawesome',
            name='READ_ME',
            field=models.TextField(default='Test', editable=False),
        ),
        migrations.AddField(
            model_name='updatefontawesome',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='READ_ME',
            field=models.TextField(default='test', editable=False),
        ),
    ]
