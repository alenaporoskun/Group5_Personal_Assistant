# Generated by Django 5.0.4 on 2024-05-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0006_alter_category_user_alter_file_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]