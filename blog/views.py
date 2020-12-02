from django.shortcuts import render, HttpResponse
from blog.models import Post
from django.db import IntegrityError
from django.contrib import messages

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
        author=request.POST.get('author1')
        slug =request.POST.get('slug1')
        timeStamp=request.POST.get('timeStamp')
        # print(title1, content1, author1, slug1)

        addpost = Post(sno=sno, title=title, content=content, author=author, slug=slug, timeStamp=timeStamp)
        addpost.save()
        
    else:
        return HttpResponse('404 Page Not Found')
    return render(request, 'blog/addBlogPost.html')


    # try:
    #     title = request.POST["title"]
    # except KeyError:
    #     title = "Guest"

# def addBlogPost(request):
    
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     author = request.POST.get('author')
#     slug = request.POST.get('slug')
#     print(title, content, author, slug)

#     addpost = Post(title=title, content=content, author=author, slug=slug)
#     addpost.save()
#     messages.success(request, "your form has been submitted")
    
#     return HttpResponse('404 Page Not Found')
#     return render(request, 'blog/addBlogPost.html')