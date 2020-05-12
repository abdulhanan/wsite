from django.shortcuts import render
from .models import cat,experience
from locations.models import location
# Create your views here.
def index(request):
    cats=cat.objects.all()
    loc=location.objects.all()
    exp=experience.objects.all()
    return render(request,"experiencelist.html", {'cat':cats, 'loc': loc,'exp': exp} )

def categories(request, slug):
    
    getid=0
    slug=slug.lower()

    catt=cat.objects.filter(
        slug=slug
    ).values('id')
    for fcat in catt:
        print(fcat['id'])
        getid=fcat['id']
    
    exp=experience.objects.filter(
        cat=getid
    )
    print(getid)
    print("this is somethingggggggggggggg")
    for fcat in exp:
        print(fcat)
        
        
    
    
    return render(request,"experiencecategorieslist.html", {'cat':exp} )


def details(request, slug):
    slug=slug.lower()
    exp = experience.objects.get(slug=slug)
    print(slug)
    return render(request,"experiencedetails.html", {'exp': exp})
    
def locdetails(request, slug):
    getid=0
    slugg=slug.lower()

    locc=location.objects.filter(
        slug=slug
    ).values('id')
    for floc in locc:
        print(floc['id'])
        getid=floc['id']
    
    exp=experience.objects.filter(
        location=getid
    )
    for floc in exp:
        print(floc)
    
    
    #exp = experience.objects.get(location=slugg)
    return render(request,"experiencelocationlist.html", {'namee':exp})
    

