# Generated by Django 3.0.5 on 2020-05-11 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0009_delete_locgallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='loc',
            field=models.ManyToManyField(related_name='_location_loc_+', to='locations.location'),
        ),
    ]
