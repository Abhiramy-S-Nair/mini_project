# Generated by Django 4.2.5 on 2023-09-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='', max_length=100),
        ),
    ]