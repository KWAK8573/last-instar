from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from myMember.models import Profile
from django.contrib import messages

def index(request):
    posts = Post.objects.all().order_by('-id')
    app_url = request.path

    conn_user = request.user
    conn_profile = Profile.objects.get(user=conn_user)

    if not conn_profile.profile_image:
        pic_url = ""
    else:
        pic_url = conn_profile.profile_image.url
            
    context = {
        'id' : conn_user.username,
        'nick' : conn_profile.nick,
        'profile_pic' : pic_url,
        'intro' : conn_profile.intro,
        'posts' : posts,
        'app_url' : app_url,
    }
    return render(request, 'index.html', context=context)

def post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid(): 
            post = form.save(commit = False)
            post.create_user = User.objects.get(username = request.user.get_username())
            post.save()
        return redirect(reverse('index'))
    else:
        form = PostForm() 
        return render(request, 'post.html', {'form' : form})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detail.html', {'post': post})