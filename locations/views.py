from django.shortcuts import render
from .models import location
from rest_framework import viewsets
from .serializers import locationSerializer
import cv2, os,glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.
loc1=location.objects.all()

class LocationApiView(viewsets.ModelViewSet):
    queryset= location.objects.all()
    serializer_class = locationSerializer


def index(request):
    return render(request,"locationlist.html" ,{'loc1': loc1} )

def base(request):
    return render(request,"base.html")

def details(request, slug):
    divide=4;
    slug=slug.lower()
    lc = location.objects.get(slug=slug)
    olc = location.objects.filter(loc=lc.id)
    numloc=len(olc)

    if ( numloc >4 ):
        numloc=4
    

    path=(BASE_DIR+"\\media\\pics\\"+slug)

    files = []
    nfiles=[]
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                
                file="/media/pics/"+slug+'/'+file
                files.append(file)

    
    context={'galimgs':files,"lc":lc,'olc':olc,'numloc':numloc}

    print(divide)
    return render(request,"locationdetails.html" ,context )
   

