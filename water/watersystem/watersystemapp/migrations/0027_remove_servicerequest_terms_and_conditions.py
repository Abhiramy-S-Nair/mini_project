# Generated by Django 4.2.5 on 2023-11-07 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0026_servicerequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='terms_and_conditions',
        ),
    ]
