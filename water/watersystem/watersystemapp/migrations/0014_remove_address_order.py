# Generated by Django 4.2.5 on 2023-11-03 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0013_address_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='order',
        ),
    ]
