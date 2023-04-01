from django.contrib import admin
from .models import Link, Comment


# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')
    search_fields = ("title", "description")


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'link', 'created')


admin.site.register(Link, LinkAdmin)
admin.site.register(Comment, CommentAdmin)
