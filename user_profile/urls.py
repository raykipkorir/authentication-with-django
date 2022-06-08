from django.urls import path
from . import views


app_name = "user_profile"
urlpatterns = [
    path("feed/", views.feed, name="feed"),
    path("profile/", views.profile, name="profile"),
]
