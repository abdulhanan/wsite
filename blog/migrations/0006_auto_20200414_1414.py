# Generated by Django 3.0.5 on 2020-04-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200414_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='starttext',
            field=models.CharField(max_length=85),
        ),
    ]
