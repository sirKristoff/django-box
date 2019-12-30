from django.contrib import admin
from .models import SearchQuery


@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'path', 'user', 'query')
    list_filter = ('path', 'user', 'timestamp')
    search_fields = ('query',)
    ordering = ('path', '-timestamp')
