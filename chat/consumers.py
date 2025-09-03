from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import GroupChat, Message
import json


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_id = self.scope["url_route"]["kwargs"]["group_id"]
        self.room_group_name = f"chat_{self.group_id}"

        user = self.scope["user"]
        group = await database_sync_to_async(GroupChat.objects.get)(pk=self.group_id)
        is_member = await database_sync_to_async(group.members.filter(id=user.id).exists)()
        if not is_member:
            await self.close()
            return

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def save_message(self, user, group_id, content):
        group = GroupChat.objects.get(pk=group_id)
        return Message.objects.create(group=group, sender=user, content=content)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        user = self.scope["user"]
        msg = await self.save_message(user, self.group_id, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": msg.content,
                "username": msg.sender.username,
                "timestamp": msg.timestamp.strftime("%H:%M"),
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "username": event["username"],
            "timestamp": event["timestamp"],
        }))
