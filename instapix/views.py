from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, PostForm, LikeForm, CommentForm
from .models import User, PostModel, LikeModel, CommentModel
from django.contrib.auth import authenticate, login, logout as dlogout


def signup(request):
    context = {}
    return render(request, 'sign-up.html', context)

def home(request):
	context = {}
	if request.user.is_authenticated:
		user = User.objects.filter(username=request.user.username)[0]
		if u.profilepic == "":
			u.profilepic = "static/assets/img/default.png"
		context = { 'user': request.user, 'ProfilePic': u.profilepic }
		return render(request, 'logged-in-index.html', context)

	return render(request, 'index.html', context)

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

def upload(request):
	form = UploadForm()
	print(form.media)
	return render(request, 'upload.html', { 'form': form })

def logout(request):
	context = {}
	dlogout(request)
	return redirect(home)