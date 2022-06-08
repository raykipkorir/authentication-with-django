from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from authentication_app.forms import EditForm, SignupForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordChangeForm


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Account created successfully")
                return redirect("user_profile:feed")

        else:
            form = SignupForm()
        return render(request, "authentication_app/signup.html", {"form": form})
    else:
        return redirect("user_profile:feed")


def home(request):
    return render(request, "authentication_app/home.html")


@login_required(login_url=reverse_lazy("django.contrib.auth:login"))
def edit_user(request, id):
    if request.method == "POST":
        user_data = get_object_or_404(User, pk=id)
        form = EditForm(request.POST, instance=user_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Account updated successfully")
    else:
        user_data = get_object_or_404(User, pk=id)
        form = EditForm(instance=user_data)
    return render(request, "authentication_app/update.html", {"form": form})


@login_required(login_url=reverse_lazy("django.contrib.auth:login"))
def delete_user(request, id):
    if request.method == "POST":
        user_data = get_object_or_404(User, pk=id)
        user_data.delete()
        return redirect("django.contrib.auth:login")
    else:
        return render(request, "authentication_app/delete.html")


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("authenticate_app:password_success")
    template_name = "registration/change_password.html"


@login_required(login_url=reverse_lazy("django.contrib.auth:login"))
def password_success(request):
    return render(request, "authentication_app/password_success.html")
