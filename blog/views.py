from django.shortcuts import render, HttpResponse
from blog.models import Post



def bloghome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/bloghome.html', context)


def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    context={'post': post}
    return render(request, 'blog/blogpost.html',context)




