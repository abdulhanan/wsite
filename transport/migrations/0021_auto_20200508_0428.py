# Generated by Django 3.0.5 on 2020-05-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0020_auto_20200508_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportbooking',
            name='transport',
            field=models.IntegerField(blank=True, default=99, null=True),
        ),
    ]
