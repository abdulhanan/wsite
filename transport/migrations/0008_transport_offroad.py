# Generated by Django 3.0.5 on 2020-05-07 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0007_auto_20200507_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='offroad',
            field=models.BooleanField(default=False),
        ),
    ]
