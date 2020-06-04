from django.shortcuts import render
#    v-- current directory
from .models import Post

def generic(request):
    return render(request, 'blog/generic.html', {})

def post_list(request):
    #args = Post.objects.all()
    #titles = {'title':args}
    #return render(request, 'blog/post_list_template.html', titles)
    posts = Post.objects.order_by('created_date')
    #<QuerySet [<Post: Test Post>, <Post: WA#8 Rough draft>, <Post: poster>, <Post: Bard>, <Post: Blogger>, <Post: Sample Text>, <Post: ABC>]>
    return render(request, 'blog/post_list_template.html', {'posts':posts})
