from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        labels = {"email": "E-mail"}
        widgets = {
            "email":forms.EmailInput(attrs={"placeholder":"example@gmail.com"})
        }


class EditForm(forms.ModelForm):
    class Meta(SignupForm.Meta):
        pass

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput(),label="Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(),label="Password Confirmation")