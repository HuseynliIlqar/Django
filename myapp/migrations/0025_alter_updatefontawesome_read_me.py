# Generated by Django 5.2 on 2025-04-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_alter_updatefontawesome_read_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatefontawesome',
            name='READ_ME',
            field=models.TextField(default='Buradan saytdakı ikonların çağırıldığı plugini sadəcə aşağıdakı URL-i dəyişərək update edə bilərsiniz.\n\nBəs necə update edək? Mən sizə sadəcə linkdəki rəqəmləri dəyişməyinizi tövsiyə edirəm:\nhttps://cdnjs.cloudflare.com/ajax/libs/font-awesome/<VERSIYA>/css/all.min.css', editable=False),
        ),
    ]
