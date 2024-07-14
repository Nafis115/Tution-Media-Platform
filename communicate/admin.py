from django.contrib import admin
from .models import Conversation, Messages

class MessagesInline(admin.TabularInline):
    model = Messages
    extra = 1

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'participants_display', 'message_count')
    search_fields = ('participants__username',)
    inlines = [MessagesInline]

    def participants_display(self, obj):
        return ", ".join([user.username for user in obj.participants.all()])
    participants_display.short_description = 'Participants'

    def message_count(self, obj):
        return obj.messages.count()
    message_count.short_description = 'Number of Messages'

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'sender', 'content', 'timestamp')
    search_fields = ('sender__username', 'content')
    list_filter = ('timestamp',)
