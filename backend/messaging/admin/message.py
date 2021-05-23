from django.contrib import admin
from messaging.models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'flag_sent', 'flag_read', 'created_at', 'updated_at',)
    