from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request, 'index.html')
@login_required(login_url='/accounts/login/')
 