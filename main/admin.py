from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    exclude = ['']
    prepopulated_fields = {'slug': ('title',)}
    empty_value_display = 'X-empty-X'

    date_hierarchy = 'created_date'

    search_fields = ('title', 'author', )
    list_display = ('title', 'author', 'created_date', 'published_date',)
    list_filter = ('author', 'created_date', 'published_date',)

admin.site.register(Article, ArticleAdmin)
