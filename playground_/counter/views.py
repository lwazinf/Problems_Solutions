from django.shortcuts import render
from search.models import post

# Create your views here.

def count(request):
    context = {
        'object': post.objects.get(id=1)
    }
    if request.method == 'POST':
        Post = post.objects.get(id=1)
        Post.applications += 1
        Post.save()
    return render(request, "counter/index.html", context)
