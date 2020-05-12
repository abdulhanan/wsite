from django.shortcuts import render
from locations.models import location
from .models import transport
from .forms import TransportBookingForm

# Create your views here.


def index(request):
    loc=location.objects.all()
    return render(request,"transportindex.html" , { 'loc': loc} )


def transportdetails(request,slug):
    slug=slug.lower()
    trans=transport.objects.get(slug=slug)    
    return render(request,"transportdetails.html" , { 'trans': trans} )


def book(request,slug):
    slug=slug.lower()
    trans=transport.objects.get(slug=slug)

    form=TransportBookingForm()
    
    if request.method=='POST':
        
        print(request.POST)
        form =TransportBookingForm(request.POST)
        if form.is_valid():
            print("before saving")
            obj=form.save(commit=False)
            obj.transport=trans.id

            obj.save()
    
    return render(request,"transportbook.html" , { 'trans': trans,'form':form} )


def locdetails(request, slug):
    getid=0
    slugg=slug.lower()

    locc=location.objects.filter(
        slug=slug
    ).values('id')

    locname=location.objects.filter(
        slug=slug
    ).values('name')
    
    locname=(locname[0]['name'])
    print(locname)
    print(locc[0]['id'])

    
    trans=transport.objects.filter(
        location=locc[0]['id']
    )
    #for floc in trans:
        #print(floc.type)
    
    
    #exp = experience.objects.get(location=slugg)
    return render(request,"transportlist.html", {'namee':trans,'locname':locname})