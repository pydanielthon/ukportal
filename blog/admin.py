from django.contrib import admin

# Register your models here.
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('imię', 'treść', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('imię', 'email', 'treść')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)