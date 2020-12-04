from django.shortcuts import render, HttpResponse
from blog.models import Post
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts' : allPosts}
    return render(request, 'blog/blogHome.html', context)
    

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    # print(post)
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)


def addBlogPost(request):
    
    if request.method == 'POST':
        sno=request.POST.get('sno')
        title=request.POST.get('title1')
        content=request.POST.get('content1')
        # author=request.POST.get('author1')
        author = request.user
        slug =request.POST.get('slug1')
        timeStamp=request.POST.get('datetimepicker')
        print(title, content, author, slug)

        addpost = Post(sno=sno, title=title, content=content, author=author, slug=slug, timeStamp=timeStamp)
        addpost.save()
        
    else:
        return HttpResponse('404 Page Not Found')
    return render(request, 'blog/blogHome.html')

