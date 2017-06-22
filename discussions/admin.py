from django.contrib import admin
from .models import Discussion, Comment, SubComment

# Register your models here.


class SubCommentInline(admin.StackedInline):
    model = SubComment
    extra = 0


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class DiscussionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'slug', 'body', 'creater']}),
        ('Other Details', {
            'classes': ('collapse',),
            'fields': ('created_date', 'upvotes', 'downvotes', 'voters', 'tags'),
        }),
    ]

    search_fields = ('title', 'creater', )
    list_display = ('title', 'creater', 'created_date',)
    list_filter = ('creater', 'created_date',)

    prepopulated_fields = {"slug": ("title",)}

    inlines = [CommentInline, SubCommentInline]

    empty_value_display = 'X-empty-X'
    date_hierarchy = 'created_date'

admin.site.register(Discussion, DiscussionAdmin)
