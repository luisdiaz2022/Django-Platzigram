"""Post admin classes."""

# Django
from django.contrib import admin

# Models

from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('pk', 'user', 'profile', 'title', 'photo')
    list_display_links = ('pk', 'user', 'profile')
    list_editable = ('title', 'photo')
    search_fields = (
        'user__username',
        'user__email', 
    )

    list_filter = (
        'user',
        'created', 
        'modified',
        )
    
    fieldsets = (
        ('User info', {
            'fields': (('user', 'profile'),),
        }),
        ('Post info', {
            'fields': (
                ('title', 'photo'),
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified')