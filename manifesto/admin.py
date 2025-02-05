from django.contrib import admin
from .models import Section

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order',)
