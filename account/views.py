from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm

# Create your views here.


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})


def user_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(request, username=cd["username"], password=cd["password"])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Authenticated successfully")
            else:
                return HttpResponse("Diabled account")
        else:
            return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {"form": form})