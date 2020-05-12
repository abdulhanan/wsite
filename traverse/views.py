from django.shortcuts import render
from locations.models import location
# Create your views here.


loc1=location.objects.all()
loc2=location.objects.filter(category=1)

context={'loc1': loc1,'catloc':loc2}
def index(request):
    return render(request,"index.html",context )