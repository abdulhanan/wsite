# Generated by Django 3.0.5 on 2020-05-07 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0017_auto_20200508_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportbooking',
            name='transport',
            field=models.IntegerField(blank=True),
        ),
    ]