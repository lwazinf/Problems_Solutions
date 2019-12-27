from django.shortcuts import render, redirect
from django.db.models import Q
from .models import post

# Create your views here.

def search(request):
    cat = "id"
    context={
        'post':post.objects.all().order_by(cat),
        'request':''
    }
    if request.method == 'POST':
        if request.POST.get('rbutton', None) == 'head':
            cat = 'title'
        elif request.POST.get('rbutton', None) == 'finger':
            cat = 'id'
        if len(request.POST['search']) != 0:
            q = Q(color__icontains=request.POST['search'])
            context={
                'post':post.objects.filter(q).order_by(cat),
                'request':request.POST['search']
            }
        elif len(request.POST['search']) == 0:
            context={
                'post':post.objects.all().order_by(cat),
                'request':request.POST['search']
            }
    return render(request, "search/index.html", context)


def like(request):
    if request.method == 'POST':
        Post = post.objects.get(id=1)
        Post.applications += 1
        Post.save()
        return redirect("home")

def dislike(request):

    if request.method == 'POST':
        Post = post.objects.get(id=1)
        Post.applications -= 1
        Post.save()
        return redirect("home")
