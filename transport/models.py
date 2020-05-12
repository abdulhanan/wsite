from django.db import models
from locations.models import location

# Create your models here.

class transport(models.Model):
    TRANSPORT_CHOICES = [
    ('Coaster', "coaster"),
    ('SUV', "suv"),
    ('Jeep', "jeep"),
    ('Saloon', "saloon"),
    ('Van', "van"),
    ('Luxury', "luxuryy"),    
    ]
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=50, unique=True)
    img =models.ImageField(upload_to='pics')
    type=models.CharField(max_length=15,choices=TRANSPORT_CHOICES,default='saloon')
    numpeople= models.IntegerField()
    price=models.IntegerField()
    location=models.ManyToManyField(location)
    ac=models.BooleanField(default=True)
    offroad=models.BooleanField(default=False)
    desc=models.TextField(max_length=300)
    mileage=models.FloatField()
    rules=models.TextField(max_length=800)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class TransportBooking(models.Model):
    startdate=models.DateField()
#    datebooked=models.DateTimeField(auto_now=True)
    numdays=models.IntegerField()
    city=models.CharField(max_length=100)
    transport=models.IntegerField( null=True, blank=True)
    #transport=models.ForeignKey(transport,on_delete=models.CASCADE)

#    class Meta:
#       ordering = ['startdate']

    def __str__(self):
        return self.city
    
