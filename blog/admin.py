# Register your models here.

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from urllib.parse import urlencode
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_date"]




class CommentAdmin(admin.ModelAdmin):
    select_related = ["post"]
    # listing page customizations
    list_display = ["author", "post_"]
    # form customizations
    exclude = ["created_date"]

    # Making the post field on the list page link to atual post
    def post_(self, comment):
        url = (
            reverse("admin:blog_post_changelist") +
            "?" +
            urlencode({
                "id": comment.post.id
            })
        )
        return format_html("<a href='{}'>{}</a>", url, comment.post)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
