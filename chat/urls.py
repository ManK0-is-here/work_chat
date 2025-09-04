from django.urls import path
from .views import *

app_name = 'groups'
urlpatterns = [
    path("create/", ChatGroupCreateView.as_view(), name="group_create"),
    path("<int:pk>/", ChatGroupDetailView.as_view(), name="group_detail"),
    path("<int:pk>/edit/", GroupChatUpdateView.as_view(), name="group_edit"),
    path("<int:pk>/delete/", GroupChatDeleteView.as_view(), name="group_delete"),
    path("<int:pk>/leave/", leave_group, name="group_leave"),
    path("<int:pk>/add_member/", add_by_username, name="group_add_member"),
    path("", GroupChatListView.as_view(), name="group_list"),
    path("<int:pk>/join/", join_group, name="group_join"),
    path("<int:pk>/chat/", ChatView.as_view(), name="group_chat"),
] 
