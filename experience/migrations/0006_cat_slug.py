# Generated by Django 3.0.5 on 2020-04-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0005_cat_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='slug',
            field=models.CharField(default='camping', max_length=30),
            preserve_default=False,
        ),
    ]
