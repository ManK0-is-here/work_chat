from django.urls import path
from .views import *


urlpatterns = [
    path("create/", group_create, name="create_group"),
] 