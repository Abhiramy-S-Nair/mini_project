# Generated by Django 4.2.5 on 2023-10-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0004_rename_user_logindetail_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('district_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=100)),
            ],
        ),
    ]
