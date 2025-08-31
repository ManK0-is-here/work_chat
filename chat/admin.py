from django.contrib import admin
from .models import GroupChat


@admin.register(GroupChat)
class GroupChatAdmin(admin.ModelAdmin):
    list_display = ("name", "creator", "created_at")
    search_fields = ("name", "creator__username")   
    list_filter = ("created_at",) 
    filter_horizontal = ("members",)   