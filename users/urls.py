from django.urls import path
from users.views import *


urlpatterns = [
    path("", user_home, name="user_home"),
    path("logout/", logout_view, name="logout")

] 