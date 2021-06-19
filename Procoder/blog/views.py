from blog.models import Post
from django.shortcuts import render


# Create your views here.

def blogHome(request):
    allposts = Post.objects.all()

    context = {'allposts': allposts}
    return render(request, "blog/blogHome.html", context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, "blog/blogPost.html", context)
