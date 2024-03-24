from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sender_id = self.scope['url_route']['kwargs']['senderId']
        self.recipient_id = self.scope['url_route']['kwargs']['recipientId']
        self.chat_id = self.get_chat_id(
            int(self.sender_id), int(self.recipient_id))

        await self.channel_layer.group_add(self.chat_id, self.channel_name)
        await self.accept()

    def get_chat_id(self, user_id, other_user_id):
        return f"chat_{min(user_id, other_user_id)}_{max(user_id, other_user_id)}"

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.chat_id, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Authenticate the user
        user = self.scope['user']
        if user.is_authenticated:
            await self.save_message(user.id, self.recipient_id, message)

            await self.channel_layer.group_send(self.chat_id, {
                'type': 'chat_message',
                'message': message,
                'sender_id': user.id
            })
        else:
            print("User is not authenticated.")

    async def chat_message(self, event):
        message = event['message']
        sender_id = event['sender_id']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender_id
        }))

    @database_sync_to_async
    def save_message(self, sender_id, recipient_id, message):
        sender = User.objects.get(id=sender_id)
        recipient = User.objects.get(id=recipient_id)
        Message.objects.create(
            sender=sender, recipient=recipient, message=message)
