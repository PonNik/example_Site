from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import UserProfile, Post
from .forms import UserProfileForm, PostForm, CustomUserCreationForm


def home(request):
    return render(request,"users/home.html")


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def users(request):
    users = UserProfile.objects.all()
    return render(request=request, 
                  template_name="users/users.html", 
                  context={'users': users})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.profile)
        print(request.user.profile.photo)
    return render(request, 
                  'users/profile.html', 
                  {'form': form})


##############################################
#   Создаем работу с блогом работа со статьями
def blogs(request):
    posts = Post.objects.all()
    return render(request, 'users/blogs.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'users/create_post.html', {'form': form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('post_detail', post_id=post.id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'users/edit_post.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

#################################