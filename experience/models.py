from django.db import models
from locations.models import location

# Create your models here.

class cat(models.Model):
    name = models.CharField(max_length=30)
    img= models.ImageField(upload_to='pics')
    slug=models.CharField(max_length=30, unique=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class experience(models.Model):
    name = models.CharField(max_length=100)
    cat = models.ManyToManyField(cat)
    slug=models.SlugField(unique=True)
    details= models.CharField(max_length=800)
    img= models.ImageField(upload_to='pics')
    galleryimg=models.ImageField(upload_to='pics')
    location = models.ManyToManyField(location)
    price = models.IntegerField()
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name