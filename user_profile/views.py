from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy


@login_required(login_url=reverse_lazy("django.contrib.auth:login"))
def feed(request):
    return render(request, "user_profile/feed.html")


@login_required(login_url=reverse_lazy("django.contrib.auth:login"))
def profile(request):
    return render(request, "user_profile/profile.html")
