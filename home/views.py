from django.shortcuts import render, HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from  blog.models import Post
# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def contact(request):



    return render(request, 'home/contact.html')


def aboutus(request):
    return render(request, 'home/aboutus.html')


def serach(request):
    query=request.GET['query']
    allPosts=Post.objects.filter(title__icontains=query);
    parems={'allPosts':allPosts}
    return render(request,'home/serach.html',parems)








    
      









