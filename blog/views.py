from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post

blogdet=Post.objects.all()
def index(request):
    return render(request,"blog.html" ,{'blogdet': blogdet} )


def details(request, slug):

    slugg=slug.lower()
    Postobj = Post.objects.get(slug=slugg)
    return render(request,"blog-post.html" ,{'mains':Postobj} )
    