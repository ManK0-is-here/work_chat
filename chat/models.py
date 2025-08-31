from django.db import models
from django.contrib.auth.models import User
import uuid


class GroupChat(models.Model):

    icon = models.ImageField(
        upload_to="group_avatar", 
        null=True,
        blank=True,  
        default="group_avatar/default.png"
        )
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(
        max_length="200", 
        null=True, 
        blank=True
        )
    members = models.ManyToManyField(
        User, 
        related_name="groups_chat", 
        blank=True
        )
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        User, 
        related_name="group_created", 
        on_delete=models.CASCADE
        )

    def is_member(self, user):
        return self.members.filter(id=user.id).exists()

    def __str__(self):
        return self.name