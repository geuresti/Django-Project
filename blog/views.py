from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Post
from django.utils import timezone
from .forms import *  # PostForm, /AccountForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def redirect_home(request):
    return redirect('homepage')

def home(request, arg=""):
    if arg:
        redirect('post_titles')
    else:
        return render(request, 'blog/homepage.html')

def register(request):
     # create form, populate it w data from request
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account successfully created.')
            return redirect('create_account')
    # if GET, create blank form
    else:
        f = UserCreationForm()
    return render(request, 'blog/create_account.html', {'form':f})

def delete(request, pk=-1):
    if pk != -1:
        Post.objects.filter(pk=pk).delete()

    return redirect('post_titles')

def post_list(request):
    posts = Post.objects.order_by('created_date')[::-1]
    return render(request, 'blog/post_list_template.html', {'posts':posts})

@login_required
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


@login_required
def user_profile(request, username="default_placeholder"):
    if username != "default_placeholder":
        # check if username references a legit user
        user = get_object_or_404(User, username = username)
        if request.user.username == username:
            posts = [p for p in Post.objects.all() if p.author == user]
            return render(request, 'blog/profile.html', {'posts':posts})
        else:
            return redirect('homepage')
    else:
        # this neesd to redirect to home on argument provided *********
        return redirect('homepage')

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
