from django.urls import path, include
from users.views import *


urlpatterns = [
    path("", user_home, name="user_home"),
    path("logout/", logout_view, name="logout"),
    path("profile/", UserProfileView.as_view(),name="profile"),
    path("edit/", UserPrifileRedactView.as_view(), name="redact_profile"),
    

] 