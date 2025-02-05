from django.contrib import admin
from .models import Profile, Post, Comment, Message, Notification

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'created_at')
    list_filter = ('created_at', 'location')
    search_fields = ('user__username', 'bio', 'location')
    raw_id_fields = ('user', 'following')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'author__username')
    raw_id_fields = ('author', 'likes')

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'author__username')
    raw_id_fields = ('author', 'post')

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'content_preview', 'read', 'created_at')
    list_filter = ('created_at', 'read')
    search_fields = ('content', 'sender__username', 'recipient__username')
    raw_id_fields = ('sender', 'recipient')

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'sender', 'notification_type', 'read', 'created_at')
    list_filter = ('notification_type', 'read', 'created_at')
    search_fields = ('recipient__username', 'sender__username')
    raw_id_fields = ('recipient', 'sender', 'post')
