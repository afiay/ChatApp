from django.contrib import admin
from .models import Message

# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'message', 'timestamp')
    list_filter = ('sender', 'recipient', 'timestamp')
    search_fields = ('sender__username', 'recipient__username', 'message')
