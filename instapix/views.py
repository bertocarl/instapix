from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Post,Profile,Comment
from .forms import PostForm,LocationForm,ProfileForm,CommentForm
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
from django.contrib.auth.models import User


# Create your views here.
@login_required
def home(request):
    current_user=request.user
    posts= Post.objects.all()
    profiles= Profile.objects.all()
    form=CommentForm()
    comments=Comment.objects.all()


    return render(request,'home.html',{"posts":posts,"profiles":profiles,"form":form,"comments":comments})

@login_required(login_url='/accounts/login/')
def new_location(request):
    if request.method =='POST':
        form=LocationForm(request.POST,request.FILES)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()

        return redirect('new-post')

    else:
        form = LocationForm()

    return render(request,'new_location.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_post(request):
   user = request.user
   if request.method == 'POST':
      form = PostForm(request.POST,request.FILES)
      if form.is_valid():
         post = form.save(commit=False)
         post.author = user.profile
         post.save()
         return redirect('home')
   else:
      form = PostForm()


   context = {
      'form': form
   }

   return render(request, 'new_post.html', context)


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    current_user_id=request.user.id
    form=CommentForm()
    comments=Comment.objects.all()
    comment_number=len(comments)
    print(current_user)
   

    post_id = None
    if request.method == 'GET':
        post_id = request.GET.get('post_id')

    likes = 0
    if post_id:
        post = Post.objects.get(id=int(post_id))
        if post:
            likes = post.likes + 1
            post.likes =  likes
            post.save()
            print(likes)

        return redirect('profile.html')

    try:
        profile = Profile.objects.get(user=current_user)
        posts = Post.objects.filter(user_id=current_user_id)
        title = profile.name
        username = profile.user.username
        post_number= len(posts)
        
    except ObjectDoesNotExist:
        return redirect('edit-profile')


    return render(request,"profile.html",{"profile":profile,"posts":posts,"form":form,"post_number":post_number,"title":title,"username":username,"comments":comments,"comment_number":comment_number})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.username = current_user
            profile.save()

    else:
        form=ProfileForm()

    return render(request,'edit_profile.html',{"form":form})

def comment(request):
    print("AJAX is working")

    comment = request.GET.get('comment')
    post = request.GET.get('post')
    username = request.user

    comment = Comment(comment=comment,post=post,username=username)
    comment.save()

    recent_comment= f'{Comment.objects.all().last().comment}'
    recent_comment_user = f'{Comment.objects.all().last().username}'
    data= {
        'recent_comment': recent_comment,
        'recent_comment_user':recent_comment_user
    }

    return JsonResponse(data)

@login_required(login_url='/accounts/login/')
def explore(request):
    posts = Post.objects.all()
    form=CommentForm()
    comments=Comment.objects.all()


    return render(request,"explore.html",{"posts":posts,"form":form,"comments":comments})


@login_required(login_url='/accounts/login/')
def like(request):
    post_id = None
    if request.method == 'GET':
        post_id = request.GET.get('post_id')

    likes = 0
    if post_id:
        post = Post.objects.get(id=int(post_id))
        if post:
            likes = post.likes + 1
            post.likes =  likes
            post.save()
            print(likes)
    return HttpResponse(likes)

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        user = User.objects.filter(username=search_term)
        searched_users = Profile.objects.filter(user=user)
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"users":searched_users})

    else:
        message="Please enter a search !!"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def userprofile(request,profile_id):
    current_user=request.user
    form =CommentForm()
    comments=Comment.objects.all()

    try:
        all_posts=Post.objects.all()
        profile = Profile.objects.get(id=profile_id)
        prof_username = profile.username
        posts = Post.objects.filter(username=prof_username)
    except:
        raise ObjectDoesNotExist()
    return render(request,"user-profile.html",{"profile":profile,"posts":posts,"form":form,"comments":comments})


@login_required(login_url='/accounts/login/')
def change_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.username = current_user
            caption.save()
        return redirect('index')
    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'change_profile.html',{"form":form})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {'form': form})

