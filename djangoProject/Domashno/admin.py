from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import BlogPost, Comment, Author


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName')

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user):
            return True
        return False


admin.site.register(Author, AuthorAdmin)


class CommentBlogAdmin(admin.StackedInline):
    model = Comment
    extra = 0

    def has_add_permission(self, request, obj=None):
        if obj and (obj.author in request.user.blocked_users.all()):
            return False
        return True


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ['title', 'content']
    list_filter = (
        ('date', DateFieldListFilter),
    )
    date_hierarchy = 'date'
    inlines = [CommentBlogAdmin, ]

    def has_view_permission(self, request, obj=None):
        if obj and (obj.author in request.user.blocked_users.all()):
            return False
        return True

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author.user):
            return True
        if obj and (request.user != obj.author.user):
            self.readonly_fields = self.get_readonly_fields(request)
            return True
        return False


admin.site.register(BlogPost, BlogPostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if obj and (obj.author in request.user.blocked_users.all()):
            return False
        return True


admin.site.register(Comment, CommentAdmin)
