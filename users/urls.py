from django.urls import path
from users.views import *


urlpatterns = [
    path("", UserDoor.user_home_page, name="user_home"),
    path("register/", UserDoor.register_view, name="regster"),
    path("login/", UserDoor.login_view, name="login"),
    path("logout/", UserDoor.logout_view, name="logout"),
] 