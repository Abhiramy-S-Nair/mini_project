# Generated by Django 4.2.5 on 2023-11-08 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0027_remove_servicerequest_terms_and_conditions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('pdf_file', models.FileField(upload_to='uploads/pdf/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
