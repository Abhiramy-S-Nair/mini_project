# Generated by Django 4.2.5 on 2023-11-05 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0021_remove_order_special_instructions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='locality',
        ),
    ]