from django.shortcuts import render, get_object_or_404, redirect
#    v-- current directory
from .models import Post
from django.utils import timezone
from .forms import PostForm

def redirect_home(request):
    return redirect('homepage')

def home(request):
    return render(request, 'blog/homepage.html', {})

def post_list(request):
    #args = Post.objects.all()
    #titles = {'title':args}
    #return render(request, 'blog/post_list_template.html', titles)
    posts = Post.objects.order_by('created_date')
    #<QuerySet [<Post: Test Post>, <Post: WA#8 Rough draft>, <Post: poster>, <Post: Bard>, <Post: Blogger>, <Post: Sample Text>, <Post: ABC>]>
    return render(request, 'blog/post_list_template.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def projects_page(request):
    return render(request, 'blog/projects.html', {})
