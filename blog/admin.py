from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'short_discription', 'is_published']
    search_fields = ['title', 'owner__name']
    list_filter = ['is_published']
    fields = ['title', 'discription', 'owner', 'is_published', 'short_discription', 'picture']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'is_published']
    raw_id_fields = ['post']
    search_fields = ['comment_text']
    list_filter = ['is_published']
    fields = ['post', 'is_published', 'comment_text']



