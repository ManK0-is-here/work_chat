from django.urls import path
from .views import *


urlpatterns = [
    path("create/", ChatGroupCreateView.as_view(), name="group_create"),
    path("<int:pk>/", ChatGroupDetailView.as_view(), name="group_detail"),

] 