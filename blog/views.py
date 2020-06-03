from django.shortcuts import render
from .models import Post

def generic(request):
    return render(request, 'blog/generic.html', {})

def post_list(request):
    args = Post.objects.all()
    titles = {'titles':args}
    return render(request, 'blog/post_list_template.html', titles)
