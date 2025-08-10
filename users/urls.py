from django.urls import path
from users.views import *


urlpatterns = [
    path("", user_home_page, name="user_home")
] 