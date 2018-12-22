from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def preview(request):
    posts = Post.objects.all()
    return render(request, "myapp/blog.html", {'posts':posts})

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form.save()
        return HttpResponse("thanks !!")
    form = PostForm()
    return render(request, "myapp/new.html", {'form': form})