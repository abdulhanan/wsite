from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=30)
    img= models.ImageField(upload_to='pics',blank=True)
    slug=models.CharField(max_length=30, unique=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class location(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    simg= models.ImageField(upload_to='pics')
    desc= models.TextField()
    desc2= models.TextField(default='default')
    slug=models.CharField(max_length=100)
    category=models.ManyToManyField(category)
    temp=models.TextField
    loc=models.ManyToManyField('self')
    
    def __str__(self):
      return self.name
    


