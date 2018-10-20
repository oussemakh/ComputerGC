from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('Title','Disc','Date')
    list_display_links = ('Date',)
    list_editable = ("Title",)
    list_filter = ('Date','Title',)
    search_fields = ['title','Date', 'slug', 'Disc']

admin.site.register(Article, ArticleAdmin)