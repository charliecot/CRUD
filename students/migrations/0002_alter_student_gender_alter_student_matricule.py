# Generated by Django 4.1.7 on 2023-04-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='matricule',
            field=models.CharField(max_length=100),
        ),
    ]