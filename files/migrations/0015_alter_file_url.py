# Generated by Django 5.0.4 on 2024-05-06 11:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0014_alter_file_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='url',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
