# Generated by Django 5.0.4 on 2024-05-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0016_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
