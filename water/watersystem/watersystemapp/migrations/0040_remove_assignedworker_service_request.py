# Generated by Django 4.2.5 on 2023-11-23 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0039_assignment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignedworker',
            name='service_request',
        ),
    ]
