# Generated by Django 3.0.5 on 2020-04-18 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='type',
            field=models.CharField(choices=[('Coaster', 'coaster'), ('SUV', 'suv'), ('Jeep', 'jeep'), ('Saloon', 'saloon'), ('Van', 'van'), ('Luxury', 'luxuryy')], default='saloon', max_length=15),
        ),
    ]
