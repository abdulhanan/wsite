# Generated by Django 3.0.5 on 2020-05-07 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0006_transport_rules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]