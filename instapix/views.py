from django.shortcuts import render, redirect
from .forms import PostForm, LikeForm, CommentForm
from .models import User, Post, Like, Comment
from django.contrib.auth import authenticate, login, logout as dlogout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# Create your views here.
def index(request):
    current_user=request.user
    posts= Post.objects.all()
    profiles= Profile.objects.all()
    form=CommentForm()
    comments=Comment.objects.all()


    return render(request,'index.html',{"post":post,"profile":profile,"form":form,"comment":comment})
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request, username):
	if User.objects.filter(username=username).exists():
		u = User.objects.filter(username=username)[0]
		if not Followers.objects.filter(user=username, follower=request.user.username).exists():
			following = "Follow"
		else:
			following = "Unfollow"

		if u.profilepic == "":
			u.profilepic = "static/assets/img/default.png"
		context = { "ProfilePic": u.profilepic, "whosprofile": username, "logged_in_as": request.user.username, "following": following }
		if request.user.is_authenticated:
			return render(request, 'logged-in-profile.html', context)
		return render(request, 'profile.html', context)
	else:
		return redirect(home)


@login_required()
def post_view(request):
    user = check_validation(request)

    if user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                image = form.cleaned_data.get('image')
                caption = form.cleaned_data.get('caption')
                post = PostModel(user=user, image=image, caption=caption)
                post.save()

                path = str(BASE_DIR + post.image.url)

                client = ImgurClient('309da390c4f405d', '0b1e627021ab1fee1c9ae9ed90eaf1565ee0e0f1')
                post.image_url = client.upload_from_path(path,anon=True)['link']
                post.save()

                return redirect('/feed/')

        else:
            form = PostForm()
        return render(request, 'index.html', {'form' : form})
    else:
        return redirect('accounts/login/')

@login_required
def feed_view(request):
    user = check_validation(request)
    if user:

        posts = PostModel.objects.all().order_by('-created_on',)

        for post in posts:

            existing_like = LikeModel.objects.filter(post_id=post.id, user=user).first()
            if existing_like:
                post.has_liked = True


        return render(request, 'feed.html', {'posts': posts})
    else:

        return redirect('accounts/login/')




def like_view(request):
    user = check_validation(request)
    if user and request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post').id
            existing_like = LikeModel.objects.filter(post_id=post_id, user=user).first()
            if not existing_like:
                LikeModel.objects.create(post_id=post_id, user=user)
            else:
                existing_like.delete()

            return redirect('/feed/')

    else:
        return redirect('/login/')


def comment_view(request):
    user = check_validation(request)
    if user and request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post').id
            comment_text = form.cleaned_data.get('comment_text')
            comment = CommentModel.objects.create(user=user, post_id=post_id, comment_text=comment_text)
            comment.save()
            # TODO: ADD MESSAGE TO INDICATE SUCCESS
            return redirect('/feed/')
        else:
            # TODO: ADD MESSAGE FOR FAILING TO POST COMMENT
            return redirect('/feed/')
    else:
        return redirect('/login')
