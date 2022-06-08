from django.urls import path
from . import views


app_name = "authenticate_app"
urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("update_profile/<int:id>/", views.edit_user, name="update_profile"),
    path("delete_user/<int:id>/", views.delete_user, name="delete_user"),
    path("password_change/", views.PasswordChangeView.as_view(), name="change_password"),
    path("password_success/", views.password_success, name="password_success"),
]
